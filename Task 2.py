# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset
df = pd.read_csv(Titanic-Dataset.csv')

# Generate summary statistics
print("Summary Statistics:")
print(df.describe())

# Create histograms for numeric features
sns.histplot(x='Age', data=df, bins=20, kde=True)
plt.title('Age Distribution')
plt.show()

sns.histplot(x='Fare', data=df, bins=20, kde=True)
plt.title('Fare Distribution')
plt.show()

# Create boxplots for numeric features
sns.boxplot(x='Age', data=df)
plt.title('Age Boxplot')
plt.show()

sns.boxplot(x='Fare', data=df)
plt.title('Fare Boxplot')
plt.show()

# Use pairplot for feature relationships
sns.pairplot(df[['Age', 'Fare', 'Survived']], hue='Survived')
plt.show()

# Calculate correlation matrix
correlation = df[['Age', 'Fare']].corr()
print("Correlation Matrix:")
print(correlation)

# Identify patterns, trends, or anomalies in the data
print("Missing Values:")
print(df.isnull().sum())

# Make basic feature-level inferences from visuals
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title('Survival Count by Sex')
plt.show()

sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title('Survival Count by Pclass')
plt.show()
