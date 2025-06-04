# 📊 Edulytics - Student Performance Analyzer

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)

A modern, intelligent web application built with Flask that analyzes student marksheet data, predicts future performance using machine learning, and generates comprehensive reports with beautiful visualizations.


## 🚀 Features

- **📁 Multi-Format Upload**: Support for CSV, XLSX, XML, and JSON file formats
- **📊 Intelligent Analysis**: Automatic calculation of totals, percentages, and performance tags
- **🤖 ML-Powered Predictions**: Linear regression model for future score prediction
- **🚨 Smart Notifications**: Automatic identification and flagging of underperforming students
- **📈 Visual Analytics**: Interactive charts showing top performers and trends
- **📄 Professional Reports**: Generate and download comprehensive PDF reports
- **🌙 Modern UI**: Sleek dark-themed interface with responsive design
- **📱 Mobile Friendly**: Optimized for both desktop and mobile devices

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn
- **Visualization**: Matplotlib, Seaborn
- **PDF Generation**: xhtml2pdf
- **Frontend**: HTML5, CSS3, JavaScript
- **Fonts**: DM Sans, Inter (Google Fonts)
- **Database**: MongoDB (Optional)

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## ⚡ Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/shreyansh-gupta-hub/edulytics.git
cd edulytics
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create Required Directories

```bash
mkdir uploads
mkdir -p static/plots
```

### 4. Environment Setup (Optional)

Create a `.env` file for MongoDB configuration:

```bash
MONGO_URI=your_mongodb_connection_string
```

### 5. Run the Application

```bash
python app.py
```

Visit `http://localhost:5000` in your browser to access Edulytics.

## 📁 Project Structure

```
edulytics/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (optional)
├── uploads/                  # Directory for uploaded files
├── static/
│   └── plots/               # Generated matplotlib/seaborn plots
└── templates/
    ├── index.html           # File upload interface
    ├── dashboard.html       # Main dashboard with analytics
    └── report_template.html # PDF report template
```

## 📊 File Format Requirements

### Supported Formats
- `.csv` (Comma Separated Values)
- `.xlsx` (Excel Spreadsheet)
- `.xml` (Extensible Markup Language)
- `.json` (JavaScript Object Notation)

### Required Structure

Your data file must follow this structure:

| Column Position | Field Name | Description | Type |
|----------------|------------|-------------|------|
| 1st Column | RollNo | Student roll number | String/Number |
| 2nd Column | Name | Student name | String |
| 3rd+ Columns | Subjects | Subject scores | Numeric |

### Example CSV Format

```csv
RollNo,Name,Maths,Physics,Chemistry,English
1,Shreyansh,89,91,85,90
2,Riya,85,88,82,87
3,Arjun,78,82,79,85
4,Priya,92,89,94,88
```

### Data Validation Rules

- First row must contain headers
- Roll numbers should be unique
- Subject scores must be numeric values
- Missing values will be handled automatically

## 🎯 Usage Guide

### Step 1: Upload Data
1. Navigate to the home page
2. Click "Choose File" and select your CSV/XLSX/XML/JSON file
3. Click "Upload and Analyze"

### Step 2: View Analytics
- **Performance Overview**: View calculated totals and percentages
- **Top Performers**: See charts highlighting best-performing students
- **Underperformer Alerts**: Automatic notifications for students needing attention
- **ML Predictions**: View predicted future performance scores

### Step 3: Generate Reports
1. Click "Download Report" button
2. Get a comprehensive PDF with all analytics and visualizations

## 🔮 ML Features

### Linear Regression Model
- Predicts future academic performance
- Based on current subject scores
- Identifies performance trends
- Provides confidence intervals

### Performance Classification
- **Excellent**: 90%+ average
- **Good**: 80-89% average  
- **Average**: 70-79% average
- **Needs Improvement**: Below 70% average

## 🎨 UI/UX Features

- **Dark Theme**: Easy on the eyes with professional appearance
- **Neon Accents**: Cyan highlights for better visual hierarchy
- **Responsive Cards**: Hover effects and smooth transitions
- **Mobile Optimized**: Works seamlessly across all devices
- **Accessibility**: Screen reader friendly with proper ARIA labels

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `MONGO_URI` | MongoDB connection string | None (Optional) |
| `FLASK_ENV` | Flask environment | `development` |
| `UPLOAD_FOLDER` | Upload directory path | `uploads/` |

### Customization Options

- Modify `static/plots/` for custom chart styling
- Update `templates/` for UI customization
- Adjust ML parameters in `app.py`

## 🚀 Future Roadmap

- [ ] **Enhanced Database**: Full MongoDB integration for data persistence
- [ ] **Multi-Semester**: Support for analyzing multiple academic terms
- [ ] **Advanced Formats**: Additional file format optimizations
- [ ] **ML Improvements**: Advanced algorithms like Random Forest and Neural Networks
- [ ] **Email Alerts**: Automatic performance notifications to parents/teachers
- [ ] **Admin Dashboard**: Multi-class comparison and historical analysis
- [ ] **API Endpoints**: RESTful API for third-party integrations
- [ ] **Real-time Analytics**: Live dashboard updates

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Bug Reports & Feature Requests

Please use the [GitHub Issues](https://github.com/shreyansh-gupta-hub/edulytics/issues) page to report bugs or request new features.

## 📞 Support

If you need help or have questions:

- 📧 Open an issue on GitHub
- 💬 Check existing discussions
- 📖 Review the documentation

## 👨‍💻 Author

**Shreyansh Gupta**

- 🌐 **Portfolio**: [shreygupta.vercel.app](https://shreygupta.vercel.app)
- 💼 **LinkedIn**: [Shreyansh Gupta](www.linkedin.com/in/shreyansh-gupta-b066b5249)
- 🐙 **GitHub**: [@shreyansh-gupta-hub](https://github.com/shreyansh-gupta-hub)

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

Made with ❤️ by [Shreyansh Gupta](https://shreygupta.vercel.app)

</div>
