Overview:
This Django project allows users to upload CSV files for analysis. The application performs basic data analysis, including generating summary statistics, detecting missing values, and visualizing data through histograms for numerical columns.

Features:
File Upload: Upload CSV files through a simple form.
Data Analysis: View the first few rows, summary statistics, and missing values of the uploaded data.
Data Visualization: Generate histograms for numerical columns and display them on the results page.

Installation:
Clone the Repository
git clone https://github.com/Nilesh5168/csv-analysis.git
cd csv-analysis
Create a Virtual Environment:
python -m venv venv
Activate the Virtual Environment:
venv\Scripts\activate

Install Dependencies:
pip install -r requirements.txt
Run Migrations:
python manage.py migrate
Run the Development Server:
python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser to access the application.

Usage:
Upload a CSV File-
Navigate to the home page.
Use the file upload form to select and upload a CSV file.

View Analysis Results-
After uploading, you will be redirected to the results page.
The results page will display the first few rows, summary statistics, missing values, and visualizations of the data.

Configuration:
Static Files: Static files are served from the /static/ URL.
Media Files: Uploaded files and generated plots are stored in the /media/ directory.

Settings:
Modify the settings.py file to configure various settings, including allowed hosts and logging.

Contributing:
Fork the Repository
Create a New Branch
Make Your Changes
Submit a Pull Request

License:
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements:
Django Framework
Pandas for data manipulation
Matplotlib and Seaborn for data visualization
