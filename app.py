import streamlit as st
import pandas as pd
import joblib
import sqlite3

# Load trained model
model = joblib.load("improved_fitness_predictor.pkl")

st.title("🏋️‍♀️ Health & Fitness Data Analyzer")
st.write("Enter your daily stats below to predict your fitness level!")

# User inputs
sleep_hours = st.number_input("🛌 Sleep Hours", min_value=0.0, max_value=12.0, value=7.0)
steps = st.number_input("👣 Steps", min_value=0, max_value=30000, value=8000)
calories = st.number_input("🔥 Calories Burned", min_value=0, max_value=5000, value=2000)
water = st.number_input("💧 Water Intake (liters)", min_value=0.0, max_value=10.0, value=2.5)
rest_hr = st.number_input("💓 Resting Heart Rate", min_value=40, max_value=120, value=70)
workout_mins = st.number_input("🏋️ Workout Minutes", min_value=0, max_value=300, value=45)

# Predict button
if st.button("Predict Fitness Level"):
    input_data = pd.DataFrame(
        [[sleep_hours, steps, calories, water, rest_hr, workout_mins]],
        columns=["sleep_hours", "steps", "calories", "water_liters", "resting_hr", "workout_minutes"]
    )
    prediction = model.predict(input_data)[0]
    st.success(f"🏆 Predicted Fitness Level: **{prediction}**")

    # Optional: save to database
    conn = sqlite3.connect("fitness.db")
    input_data["fitness_level"] = prediction
    input_data.to_sql("predictions_log", conn, if_exists="append", index=False)
    conn.close()
    st.info("✅ Prediction saved to database!")


