# Day 5 - Machine Learning Model
# Author: Syna Shah

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Load cleaned dataset
df = pd.read_csv("cleaned_fitness_data.csv")

# 2. (Optional) Create a target variable if not present
# We'll simulate a fitness level based on steps, sleep, and calories
df['fitness_level'] = pd.cut(
    df['steps'] * 0.5 + df['sleep_hours'] * 0.3 + df['calories'] * 0.2,
    bins=3,
    labels=['Low', 'Medium', 'High']
)

# 3. Define features (X) and target (y)
X = df[['sleep_hours', 'steps', 'calories', 'water_liters', 'resting_hr', 'workout_minutes']]
y = df['fitness_level']

# 4. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 5. Train a Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 6. Make predictions
y_pred = model.predict(X_test)

# 7. Evaluate model
print("✅ Model Accuracy:", accuracy_score(y_test, y_pred))
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

# 8. Save the model for future use
import joblib
joblib.dump(model, "fitness_predictor.pkl")
print("\n💾 Model saved as 'fitness_predictor.pkl'")
