# 📊 Edulytics - Student Performance Analyzer

**Built by Shreyansh**

A modern, intelligent web application for analyzing student performance data with automated insights, grade predictions, and comprehensive reporting capabilities.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

### 📈 **Data Analysis & Visualization**
- **CSV Upload & Processing**: Upload student marksheets in CSV format
- **Automated Calculations**: Total scores, percentages, and performance metrics
- **Interactive Dashboard**: Clean, modern interface with data tables
- **Top Performers Chart**: Visual representation of highest-scoring students

### 🤖 **Machine Learning Integration**
- **Grade Prediction**: Uses Linear Regression to predict next exam scores
- **Performance Classification**: Automatically identifies underperforming students
- **Smart Analytics**: Data-driven insights for educational improvement

### 📋 **Reporting & Export**
- **PDF Report Generation**: Professional reports with charts and data
- **Performance Notifications**: Alerts for students needing attention
- **Comprehensive Analytics**: Detailed breakdown of class performance

### 🎨 **Modern UI/UX**
- **Dark Theme**: Eye-friendly design with neon accents
- **Responsive Layout**: Works seamlessly on desktop and mobile
- **Smooth Animations**: Hover effects and transitions
- **Clean Typography**: Professional fonts (DM Sans, Inter)

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/edulytics.git
   cd edulytics
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create necessary directories**
   ```bash
   mkdir uploads static/plots
   ```

4. **Set up environment variables** (optional)
   ```bash
   # Create .env file for MongoDB connection (if using)
   echo "MONGO_URI=your_mongodb_connection_string" > .env
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## 📁 Project Structure

```
edulytics/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (optional)
├── uploads/              # CSV file storage
├── static/
│   └── plots/            # Generated charts and graphs
└── templates/
    ├── index.html        # Home page with upload form
    ├── dashboard.html    # Main analytics dashboard
    └── report_template.html  # PDF report template
```

## 📊 CSV Format Requirements

Your CSV file must follow this specific format:

### Required Structure:
- **First row**: Headers
- **First column**: `RollNo` (student roll numbers)
- **Second column**: `Name` (student names)
- **Remaining columns**: Subject scores (numeric values)

### Example CSV:
```csv
RollNo,Name,Mathematics,Physics,Chemistry,Biology,English
1,Advait Kumar,78,82,80,85,79
2,Priya Sharma,85,88,82,90,87
3,Rahul Patel,72,75,78,80,74
4,Anjali Singh,90,92,88,94,89
```

### Important Notes:
- All subject scores must be **numeric values**
- Subject names can be customized (Maths, Science, History, etc.)
- Missing values will be handled automatically
- File must be saved as `.csv` format

## 🛠️ Technical Stack

### Backend:
- **Flask**: Web framework
- **Pandas**: Data manipulation and analysis
- **Scikit-learn**: Machine learning for predictions
- **NumPy**: Numerical computations

### Data Visualization:
- **Matplotlib**: Chart generation
- **Seaborn**: Statistical data visualization

### PDF Generation:
- **xhtml2pdf**: HTML to PDF conversion
- **ReportLab**: PDF styling and formatting

### Frontend:
- **HTML5/CSS3**: Modern web standards
- **Custom CSS**: Dark theme with gradient effects
- **Google Fonts**: Professional typography

## 📈 Features Breakdown

### 1. **Dashboard Analytics**
- Student performance table with all calculated metrics
- Total scores and percentage calculations
- Performance status (Good/Underperforming)
- Predicted next exam scores using ML

### 2. **Visual Charts**
- Top 5 students bar chart
- Clean, professional styling
- Automatic chart generation and updates

### 3. **PDF Reports**
- Complete student data in professional format
- Embedded charts and visualizations
- Downloadable and shareable reports

### 4. **Smart Predictions**
- Linear regression model for grade prediction
- Pattern recognition in student performance
- Early warning system for struggling students

## 🎯 Use Cases

- **Teachers**: Track student progress and identify areas for improvement
- **Schools**: Generate comprehensive class performance reports
- **Students**: Understand performance trends and predictions
- **Parents**: Monitor their child's academic progress
- **Administrators**: Analyze institutional performance metrics

## 🔧 Configuration

### Environment Variables:
```bash
# Optional MongoDB connection (for future features)
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/database

# Flask configuration
FLASK_ENV=development
FLASK_DEBUG=True
```

### Customization Options:
- Modify color scheme in CSS variables
- Adjust ML model parameters in `app.py`
- Customize PDF report template
- Add new visualization charts

## 🚀 Future Enhancements

- [ ] MongoDB integration for data persistence
- [ ] Multiple file format support (Excel, JSON)
- [ ] Advanced ML models for better predictions
- [ ] Student comparison and ranking features
- [ ] Email notifications for performance alerts
- [ ] Multi-class and multi-semester support
- [ ] Interactive charts and graphs
- [ ] User authentication and role management

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Shreyansh**
- Porfolio: [@shrey](https://shreygupta.vercel.app)
- GitHub: [@shreyansh](https://github.com/shreyansh-gupta-hub)
- LinkedIn: [Shreyansh Gupta](https://www.linkedin.com/in/data-scientist-shreyansh-gupta/)

## 🙏 Acknowledgments

- Flask community for excellent documentation
- Pandas and Scikit-learn teams for powerful data tools
- Google Fonts for beautiful typography
- All contributors and users of this project

---

⭐ **Star this repository if you found it helpful!**

For questions or support, please open an issue or contact the author.