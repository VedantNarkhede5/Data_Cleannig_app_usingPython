# Data_Cleannig_app_usingPython

🧹 CSV Data Cleaner & Visualization Tool (Python + Tkinter)

📘 Overview

This project is a Python GUI application built with Tkinter, Pandas, Matplotlib, and Seaborn.
It allows users to upload a CSV file, automatically clean the data, handle missing values intelligently, and generate visualizations.
The user can then download both the cleaned CSV file and a PDF report containing multiple data visualizations.


---

🚀 Features

✅ Upload CSV File – Select any CSV file from your computer.
✅ Automatic Data Cleaning

Removes duplicate rows

Strips extra spaces from column names

Fills missing values:

Numeric columns → Replaced with median

Categorical columns → Replaced with mode (most frequent value)


Attempts automatic data type conversion (numbers/dates)
✅ Data Preview – Shows a preview of the cleaned data inside the GUI.
✅ Download Cleaned CSV – Save the cleaned version of the dataset to your computer.
✅ Generate Visualization Report (PDF) – Creates a single PDF file with:

Histogram

Scatter Plot

Strip Plot

Box Plot



---

🖼️ Sample GUI

The application has a simple interface with:

Upload & Clean CSV button

Download Cleaned File button

Download Visualization PDF button

Text area showing the data preview and cleaning status



---

🧠 Technologies Used

Python 3.x

Tkinter → GUI framework

Pandas → Data cleaning and processing

Matplotlib & Seaborn → Data visualization

PdfPages (matplotlib.backends) → PDF report generation



---

⚙️ Installation & Setup

1. Clone the Repository

git clone https://github.com/your-username/csv-data-cleaner-visualizer.git
cd csv-data-cleaner-visualizer


2. Install Dependencies

pip install pandas matplotlib seaborn


3. Run the Application

python app.py

(Replace app.py with your actual Python filename)




---

📂 Output Files

Cleaned CSV File → Saved after data cleaning.

Visualization Report (PDF) → Includes all visual plots for quick insight.



---

📊 Example Visualizations in PDF

Histogram showing data distribution

Scatter plot between first two numeric columns

Strip plot for value spread

Box plot for detecting outliers



---

👨‍💻 Author

Vedant Narkhede
---

🏁 Future Enhancements

Add option to choose mean or median for missing numeric values

Allow custom plot selection (e.g., pairplot, heatmap)

