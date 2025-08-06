#Importing necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Loading dataset
df = pd.read_csv('Titanic-Dataset.csv')  

# Overview of data
print(df.info())

# Basic statistical summary
print(df.describe())

# Checking missing values
print(df.isnull().sum())

# Histogram for all numeric columns
df.hist(figsize=(15, 10), bins=30)
plt.suptitle("Histograms of Numeric Features")
plt.show()

# Boxplots for all numeric columns
plt.figure(figsize=(15, 10))
for i, col in enumerate(df.select_dtypes(include='number').columns):
    plt.subplot(3, 3, i+1)
    sns.boxplot(y=df[col])
    plt.title(f'Boxplot of {col}')
    plt.tight_layout()
plt.show()

# Correlation matrix
plt.figure(figsize=(12, 8))
numeric_df = df.select_dtypes(include='number')
sns.heatmap(numeric_df.corr(), annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Pairplot (Seaborn)
sns.pairplot(numeric_df)
plt.suptitle("Pairplot of Numeric Features", y=1.02)
plt.show()

# Interactive scatter matrix
fig = px.scatter_matrix(df,
                        dimensions=df.select_dtypes(include='number').columns,
                        title="Interactive Scatter Matrix")
fig.show()

# Interactive boxplot example
fig = px.box(df, y="Pclass")  
fig.show()

# Example inference
print("The correlation matrix shows that 'feature1' and 'feature2' are highly positively correlated.")
