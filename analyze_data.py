# Day 3 - Data Loading & Exploration
# Author: Syna Shah

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
df = pd.read_csv("fitness_data.csv")

# 2. View basic info
print("🔹 First 5 rows:")
print(df.head(), "\n")

print("🔹 Summary:")
print(df.describe(), "\n")

print("🔹 Column names:", df.columns.tolist(), "\n")

# 3. Check for missing values
print("🔹 Missing values per column:")
print(df.isnull().sum(), "\n")

# 4. Basic analysis
print("Average Sleep Hours:", df['sleep_hours'].mean())
print("Average Steps:", df['steps'].mean())
print("Most common Fitness Level:", df['fitness_level'].mode()[0])

# 5. Visualizations
plt.figure(figsize=(10,4))
sns.barplot(x="fitness_level", y="sleep_hours", data=df)
plt.title("Average Sleep Hours per Fitness Level")
plt.show()

# add this small pause 👇
input("Press Enter to continue to scatter plot...")

plt.figure(figsize=(10,4))
sns.scatterplot(x="steps", y="calories", hue="fitness_level", data=df)
plt.title("Steps vs Calories")
plt.show()

