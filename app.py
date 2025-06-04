from flask import Flask, render_template, request, redirect, url_for, make_response, send_file
import os
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from xhtml2pdf import pisa
from sklearn.linear_model import LinearRegression
import numpy as np
import base64
import io

# --- Flask App Config ---
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# --- Load Environment Variables ---
load_dotenv()
MONGO_URI = os.getenv("mongodb+srv://shreyanshgupta:wiwmat-vissA6-tipdyc@cluster0.ag5a91z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
print("MONGO_URI Loaded:", MONGO_URI)

# --- Routes ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('marksheet')

    if not file:
        return render_template("error.html", message="No file uploaded.")

    filename = file.filename.lower()

    try:
        if filename.endswith('.csv'):
            df = pd.read_csv(file, encoding='utf-8', engine='python', skip_blank_lines=True)
        elif filename.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(file)
        elif filename.endswith('.json'):
            df = pd.read_json(file)
        else:
            return render_template("error.html", message="Unsupported file format. Please upload CSV, Excel, or JSON files.")

        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

        if df.empty or not {'RollNo', 'Name'}.intersection(df.columns):
            return render_template("error.html", message="Uploaded file is invalid or missing required columns.")

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'latest.csv')
        df.to_csv(file_path, index=False)

    except Exception as e:
        return render_template("error.html", message=f"Error processing file: {e}")

    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    try:
        df = pd.read_csv('uploads/latest.csv', encoding='utf-8', engine='python', skip_blank_lines=True)
    except Exception as e:
        return render_template("error.html", message=f"Error reading file: {e}")

    if df.empty:
        return render_template("error.html", message="Uploaded CSV is empty.")

    exclude_columns = {'RollNo', 'Name'}
    subject_columns = [col for col in df.columns if col not in exclude_columns and pd.api.types.is_numeric_dtype(df[col])]

    if not subject_columns:
        return render_template("error.html", message="No numeric subject columns found in your dataset.")

    try:
        df['Total'] = df[subject_columns].sum(axis=1)
        df['%tage'] = df['Total'] / len(subject_columns)

        model = LinearRegression()
        X = np.arange(len(subject_columns)).reshape(-1, 1)
        predictions = []
        for _, row in df.iterrows():
            y = row[subject_columns].values.reshape(-1, 1)
            model.fit(X, y)
            pred = model.predict([[len(subject_columns)]])
            predictions.append(round(pred[0][0], 2))
        df['forecasted score'] = predictions

        df['Status'] = df['%tage'].apply(lambda x: 'Underperforming' if x < 40 else 'Good')

    except Exception as e:
        return render_template("error.html", message=f"Error calculating total/percentage: {e}")

    generate_plots(df, subject_columns)
    html_table = df.to_html(classes='data', index=False)
    return render_template("dashboard.html", table=html_table)

def generate_plots(df, subject_columns):
    if 'Name' not in df.columns:
        return

    top_students = df.nlargest(5, 'Total')

    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_students, x='Name', y='Total', palette='Blues_d')
    plt.title("Top 5 Students by Total Score")
    plt.xticks(rotation=45)
    plt.tight_layout()

    os.makedirs('static/plots', exist_ok=True)
    plt.savefig('static/plots/top_scores.png')
    plt.close()

@app.route('/download-report')
def download_report():
    try:
        df = pd.read_csv('uploads/latest.csv', encoding='utf-8', engine='python', skip_blank_lines=True)
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

        exclude_columns = {'RollNo', 'Name'}
        subject_columns = [col for col in df.columns if col not in exclude_columns and pd.api.types.is_numeric_dtype(df[col])]

        df['Total'] = df[subject_columns].sum(axis=1)
        df['%tage'] = df['Total'] / len(subject_columns)

        model = LinearRegression()
        X = np.arange(len(subject_columns)).reshape(-1, 1)
        predictions = []
        for _, row in df.iterrows():
            y = row[subject_columns].values.reshape(-1, 1)
            model.fit(X, y)
            pred = model.predict([[len(subject_columns)]])
            predictions.append(round(pred[0][0], 2))
        df['forecasted score'] = predictions
        df['Status'] = df['%tage'].apply(lambda x: 'Underperforming' if x < 40 else 'Good')

        generate_plots(df, subject_columns)

        with open('static/plots/top_scores.png', 'rb') as img_file:
            img_data = base64.b64encode(img_file.read()).decode('utf-8')
        img_src = f'data:image/png;base64,{img_data}'

        html = render_template('report_template.html',
                               table=df.to_html(index=False),
                               image=img_src)

        pdf_buffer = io.BytesIO()
        pisa_status = pisa.CreatePDF(html, dest=pdf_buffer)

        if pisa_status.err:
            return render_template("error.html", message="Error generating PDF")

        pdf_buffer.seek(0)
        return send_file(pdf_buffer,
                         as_attachment=True,
                         download_name="report.pdf",
                         mimetype='application/pdf')

    except Exception as e:
        return render_template("error.html", message=f"Error generating report: {e}")

# --- Run Server ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
