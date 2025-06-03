from flask import Flask, render_template, request, redirect, url_for
import os
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from flask import make_response
from sklearn.linear_model import LinearRegression
import numpy as np
from xhtml2pdf import pisa
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

    if not file or not file.filename.endswith('.csv'):
        return "<h2 style='color:red;'>Please upload a valid CSV file.</h2>"

    try:
        # Sanitize and save the uploaded file
        filename = 'latest.csv'  # Force all uploads to use same name
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Read and clean the CSV before saving
        df = pd.read_csv(file, encoding='utf-8', engine='python', skip_blank_lines=True)
        
        # Optional: remove unnamed index column if present
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

        df.to_csv(file_path, index=False)

    except Exception as e:
        return f"<h2 style='color:red;'>Error processing file: {e}</h2>"

    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    try:
        df = pd.read_csv('uploads/latest.csv', encoding='utf-8', engine='python', skip_blank_lines=True)
    except Exception as e:
        return f"<h2 style='color:red;'>Error reading file: {e}</h2>"

    if df.empty:
        return "<h2 style='color:red;'>Uploaded CSV is empty.</h2>"

    exclude_columns = {'RollNo', 'Name'}
    subject_columns = [col for col in df.columns if col not in exclude_columns and pd.api.types.is_numeric_dtype(df[col])]

    if not subject_columns:
        return "<h2 style='color:red;'>No numeric subject columns found in your CSV.</h2>"

    try:
        df['Total'] = df[subject_columns].sum(axis=1)
        df['Percentage'] = df['Total'] / len(subject_columns)
    except Exception as e:
        return f"<h2 style='color:red;'>Error calculating total/percentage: {e}</h2>"

    # ✅ Grade prediction using linear regression
    from sklearn.linear_model import LinearRegression
    import numpy as np
    model = LinearRegression()
    X = np.arange(len(subject_columns)).reshape(-1, 1)
    predictions = []
    for _, row in df.iterrows():
        y = row[subject_columns].values.reshape(-1, 1)
        model.fit(X, y)
        pred = model.predict([[len(subject_columns)]])
        predictions.append(round(pred[0][0], 2))
    df['Predicted Next Score'] = predictions

    # ✅ Underperforming notifications
    df['Status'] = df['Percentage'].apply(lambda x: 'Underperforming' if x < 40 else 'Good')

    # ✅ Generate updated plots
    generate_plots(df, subject_columns)

    html_table = df.to_html(classes='data', index=False)
    return render_template("dashboard.html", table=html_table)
# --- Plot Generator ---
def generate_plots(df, subject_columns):
    if 'Name' not in df.columns:
        return  # Cannot plot without names

    top_students = df.nlargest(5, 'Total')

    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_students, x='Name', y='Total', palette='Blues_d')
    plt.title("Top 5 Students by Total Score")
    plt.xticks(rotation=45)
    plt.tight_layout()

    os.makedirs('static/plots', exist_ok=True)
    plt.savefig('static/plots/top_scores.png')
    plt.close()


from flask import make_response, send_file
import io
import base64

@app.route('/download-report')
def download_report():
    df = pd.read_csv('uploads/latest.csv')

    # Encode image to base64
    with open('static/plots/top_scores.png', 'rb') as img_file:
        img_data = base64.b64encode(img_file.read()).decode('utf-8')
    img_src = f'data:image/png;base64,{img_data}'

    # Render HTML
    html = render_template('report_template.html',
                           table=df.to_html(index=False),
                           image=img_src)

    # Convert HTML to PDF using xhtml2pdf
    pdf_buffer = io.BytesIO()
    pisa_status = pisa.CreatePDF(src=html, dest=pdf_buffer)

    if pisa_status.err:
        return "<h2 style='color:red;'>Error generating PDF report.</h2>"

    pdf_buffer.seek(0)

    return send_file(pdf_buffer,
                     as_attachment=True,
                     download_name="report.pdf",)
# --- Run Server ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
