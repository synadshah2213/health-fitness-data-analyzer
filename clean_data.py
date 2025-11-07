# Day 4 - Data Cleaning & Preparation
# Author: Syna Shah

import pandas as pd
import numpy as np

# 1. Load the dataset
df = pd.read_csv("fitness_data.csv")

print("🔹 Before Cleaning:\n", df.info(), "\n")

# 2. Check for missing values
print("🔹 Missing values per column:\n", df.isnull().sum(), "\n")

# 3. Fill or remove missing values (if any)
df['sleep_hours'].fillna(df['sleep_hours'].mean(), inplace=True)
df['steps'].fillna(df['steps'].median(), inplace=True)
df['calories'].fillna(df['calories'].mean(), inplace=True)
df['water_liters'].fillna(df['water_liters'].mean(), inplace=True)
df.dropna(inplace=True)  # remove remaining null rows if any

# 4. Convert datatypes (if needed)
df['date'] = pd.to_datetime(df['date'])

# 5. Normalize numeric columns (scale 0–1)
num_cols = ['sleep_hours', 'steps', 'calories', 'water_liters', 'resting_hr', 'workout_minutes']
df[num_cols] = (df[num_cols] - df[num_cols].min()) / (df[num_cols].max() - df[num_cols].min())

# 6. Verify changes
print("🔹 After Cleaning:\n", df.info(), "\n")
print(df.head())

# 7. Save cleaned dataset
df.to_csv("cleaned_fitness_data.csv", index=False)
print("\n✅ Cleaned dataset saved as 'cleaned_fitness_data.csv'")
