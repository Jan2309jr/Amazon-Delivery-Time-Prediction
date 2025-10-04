import streamlit as st
import pandas as pd
import numpy as np
import joblib
def preprocess_features(X):
    X = X.copy()
    
    # Convert datetime columns if they exist
    datetime_cols = [col for col in X.columns if 'Date' in col or 'Time' in col]
    for col in datetime_cols:
        try:
            X[col] = pd.to_datetime(X[col], errors='coerce')
        except:
            pass
    
    # Extract datetime features
    for col in datetime_cols:
        if pd.api.types.is_datetime64_any_dtype(X[col]):
            X[col + '_hour'] = X[col].dt.hour
            X[col + '_day'] = X[col].dt.day
            X[col + '_weekday'] = X[col].dt.weekday
            X[col + '_month'] = X[col].dt.month
    
    # Drop raw datetime / string time columns
    X = X.drop(datetime_cols, axis=1)
    
    # Encode categorical features
    cat_cols = X.select_dtypes(include=['object']).columns
    for col in cat_cols:
        X[col] = X[col].astype('category').cat.codes
    
    return X


#loading the model and preproccessing
best_model = joblib.load("best_delivery_model.pkl")


st.set_page_config(page_title="Amazon Delivery Time Predictor", layout="centered")
st.title("📦 Amazon Delivery Time Prediction")

st.markdown("""
Predict estimated delivery time for your order based on agent, traffic, weather, and product details.
""")
#user inputs
with st.form("input_form"):
    st.subheader("Order Details")
    
    # Numeric Inputs
    agent_age = st.number_input("Agent Age", min_value=18, max_value=65, value=30)
    agent_rating = st.slider("Agent Rating", 1.0, 5.0, 4.0, 0.1)
    distance_km = st.number_input("Distance (km)", min_value=0.1, max_value=100.0, value=5.0)
    
    # Categorical Inputs
    weather = st.selectbox("Weather", ["Sunny", "Rainy", "Cloudy", "Stormy"])
    traffic = st.selectbox("Traffic", ["Low", "Medium", "High"])
    vehicle = st.selectbox("Vehicle", ["Bike", "Car", "Van", "Truck"])
    area = st.selectbox("Delivery Area", ["Urban", "Metropolitan", "Rural"])
    category = st.selectbox("Product Category", ["Electronics", "Clothing", "Groceries", "Other"])
    
    # Date/Time Inputs
    order_datetime = st.date_input("Order Date")
    order_time = st.time_input("Order Time")
    
    submitted = st.form_submit_button("Predict Delivery Time")
#prediction
if submitted:
    # Create DataFrame for single input
    input_df = pd.DataFrame({
        "Agent_Age": [agent_age],
        "Agent_Rating": [agent_rating],
        "Distance_km": [distance_km],
        "Weather": [weather],
        "Traffic": [traffic],
        "Vehicle": [vehicle],
        "Area": [area],
        "Category": [category],
        "Order_Date": [pd.to_datetime(order_datetime)],
        "Order_Time": [pd.to_datetime(order_time.strftime("%H:%M:%S"))]
    })

    # Preprocess input
    processed_input = preprocess_features(input_df)
    
    # Predict
    predicted_time = best_model.predict(processed_input)[0]
    
    # Display Result
    st.success(f"Estimated Delivery Time: **{predicted_time:.2f} hours** 🚚")
