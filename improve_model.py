# Day 6 - Model Testing, Improvement & Visualization
# Author: Syna Shah

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib

# 1. Load cleaned data
df = pd.read_csv("cleaned_fitness_data.csv")

# 2. Load the same fitness_level column logic
df['fitness_level'] = pd.cut(
    df['steps'] * 0.5 + df['sleep_hours'] * 0.3 + df['calories'] * 0.2,
    bins=3,
    labels=['Low', 'Medium', 'High']
)

# 3. Define X and y
X = df[['sleep_hours', 'steps', 'calories', 'water_liters', 'resting_hr', 'workout_minutes']]
y = df['fitness_level']

# 4. Split data again
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 5. Load your trained model
model = joblib.load("fitness_predictor.pkl")

# 6. Evaluate existing model
y_pred = model.predict(X_test)
print("🔹 Original Model Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 7. Create a confusion matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Low','Medium','High'], yticklabels=['Low','Medium','High'])
plt.title("Confusion Matrix - Fitness Level Prediction")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.savefig("confusion_matrix.png")
print("\n📊 Confusion matrix saved as 'confusion_matrix.png'")

# 8. Improve model with parameter tuning
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 5, 10],
    'min_samples_split': [2, 5]
}

grid = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3, scoring='accuracy')
grid.fit(X_train, y_train)

best_model = grid.best_estimator_
print("\n✅ Best Model Parameters:", grid.best_params_)

# 9. Test the improved model
y_pred_best = best_model.predict(X_test)
print("\n🔹 Improved Model Accuracy:", accuracy_score(y_test, y_pred_best))
print("\nImproved Classification Report:\n", classification_report(y_test, y_pred_best))

# 10. Feature Importance Visualization
importances = best_model.feature_importances_
features = X.columns
sns.barplot(x=importances, y=features, palette="viridis")
plt.title("Feature Importance in Fitness Prediction")
plt.tight_layout()
plt.savefig("feature_importance.png")
print("\n🌟 Feature importance chart saved as 'feature_importance.png'")

# 11. Save the improved model
joblib.dump(best_model, "improved_fitness_predictor.pkl")
print("\n💾 Improved model saved as 'improved_fitness_predictor.pkl'")
