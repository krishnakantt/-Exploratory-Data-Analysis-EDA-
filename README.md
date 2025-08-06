# 🔍 Exploratory Data Analysis (EDA) using Machine Learning
This repository showcases a detailed Exploratory Data Analysis (EDA) process using Python and key data science libraries. EDA is a crucial step in any data science or machine learning project, aimed at understanding the structure, relationships, and patterns in the dataset before model building.


## 📁 Project Structure
📦EDA-ML-Project  
 ┣ 📊 Titanic-dataset/               # Contains the dataset used  
 ┣ 📄 EDA 2.py              # Main Python Script  
 ┣ 📄 requirements.txt       # Python dependencies  
 ┗ 📄 README.md              # Project documentation  

 ## 📌 Objectives
- Understand the structure and quality of the dataset.
- Generate summary statistics (mean, median, std, etc.).
- Identify missing values and outliers.
- Visualize data distributions and correlations.
- Detect patterns and insights that guide ML model development.

## 📂 Dataset
The dataset used for this project is the Titanic - Machine Learning from Disaster dataset, a classic in the data science community. It contains data about the passengers aboard the RMS Titanic and is commonly used to explore binary classification problems — in this case, predicting survival.

## 🔢 Dataset Overview
- Rows: 891 passengers
- Columns: 12 features

## 📌 Features

| Feature       | Description |
|---------------|-------------|
| `PassengerId` | Unique ID for each passenger |
| `Survived`    | Survival status (0 = No, 1 = Yes) |
| `Pclass`      | Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd) |
| `Name`        | Full name of the passenger |
| `Sex`         | Gender (male/female) |
| `Age`         | Age of the passenger in years |
| `SibSp`       | Number of siblings/spouses aboard |
| `Parch`       | Number of parents/children aboard |
| `Ticket`      | Ticket number |
| `Fare`        | Passenger fare (in British pounds) |
| `Cabin`       | Cabin number (many missing values) |
| `Embarked`    | Port of Embarkation (`C`, `Q`, `S`) |


## ⚠️ Missing Data
Age: ~20% missing  
Cabin: ~77% missing  
Embarked: 2 missing values  

## 📊 Tools & Libraries
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly

## 📈 Visualizations Used
- Histograms
- Boxplots
- Heatmaps
- Pairplots
- Correlation Matrix
- Distribution Plots

## ⚙️ Installation
1. Clone the repository:
git clone https://github.com/krishnakantt/-Exploratory-Data-Analysis-EDA-.git
2. Install dependencies:
   pip install -r requirements.txt
3. Run the script
