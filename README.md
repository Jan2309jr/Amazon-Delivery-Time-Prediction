# Amazon Delivery Time Prediction

---

## 🎯 Problem Statement

The project focuses on predicting delivery times for e-commerce orders by analyzing multiple factors, including:

* Product size and category
* Distance between store and delivery location
* Traffic and weather conditions
* Shipping method

The goal is to preprocess the dataset, perform EDA, develop regression models, and deploy a Streamlit application where users can input order details and get estimated delivery times.

---

## 🛠️ Skills & Takeaways

* **Python Scripting**: Automating tasks, data manipulation, and analysis.
* **Data Cleaning & Preprocessing**: Handling missing values, duplicates, and standardizing categorical variables.
* **Exploratory Data Analysis (EDA)**: Identifying trends, patterns, and correlations using visualizations.
* **Feature Engineering**: Time-based features, geospatial calculations (distance between store and drop locations).
* **Machine Learning & Regression Modeling**: Linear Regression, Random Forest Regressor, Gradient Boosting Regressor.
* **MLflow**: Model tracking, comparison, and versioning.
* **Streamlit**: Building an interactive web interface for real-time predictions.

## 🌐 Domain

**E-Commerce & Logistics** – optimizing delivery schedules and improving customer satisfaction.

---

## 💼 Business Use Cases

1. **Enhanced Delivery Logistics**: Predict accurate delivery times to improve customer satisfaction.
2. **Dynamic Traffic & Weather Adjustments**: Update delivery estimates in real-time based on external conditions.
3. **Agent Performance Evaluation**: Identify areas of improvement for delivery agents.
4. **Operational Efficiency**: Optimize resource allocation and delivery planning.

---
## 🌐 App 

### App URL
[Amazon Delivery Time Prediction](https://amazondeliverytimepred.streamlit.app/)

### Images
<img width="472" height="808" alt="image" src="https://github.com/user-attachments/assets/beb16850-a3c9-4cc2-a8fc-7807c6aba5a0" />


---
## 📝 Approach

### 1. Data Preparation

* Load and inspect the dataset.
* Handle missing, inconsistent, and duplicate values.
* Standardize categorical variables like `Weather`, `Traffic`, `Vehicle`, and `Area`.

### 2. Feature Engineering

* Calculate geospatial distances using store and drop coordinates.
* Extract time-based features: hour of day, day of week, and month.
* Encode categorical variables for regression models.

### 3. Exploratory Data Analysis (EDA)

* Analyze distributions and trends in `Delivery_Time`.
* Visualize the impact of `Traffic`, `Weather`, and `Product Category` on delivery times.
* Explore agent performance and relationships between variables.

**Key Visualizations**:

* Bar charts: Delivery time by product category
* Scatter plots: Distance vs. delivery time
* Heatmaps: Correlation between agent rating and delivery time

### 4. Regression Model Development

* Models developed:

  * Linear Regression
  * Random Forest Regressor
  * Gradient Boosting Regressor
* Evaluate performance using:

  * **RMSE (Root Mean Squared Error)**
  * **MAE (Mean Absolute Error)**
  * **R² Score**
* Track models using **MLflow** for comparison and versioning.

### 5. Application Development

* Streamlit interface for end-users:

  * Input order details (distance, traffic, weather, etc.)
  * Display predicted delivery times dynamically

### 6. Deployment

* Deploy the Streamlit application for accessibility and scalability.

---

## 📊 Dataset

**File**: `amazon_delivery.csv`

**Columns & Description**:

| Column                   | Description                                    |
| ------------------------ | ---------------------------------------------- |
| Order_ID                 | Unique identifier for each order               |
| Agent_Age                | Age of the delivery agent                      |
| Agent_Rating             | Rating of the delivery agent                   |
| Store_Latitude/Longitude | Store geolocation                              |
| Drop_Latitude/Longitude  | Delivery location geolocation                  |
| Order_Date/Order_Time    | Timestamp when the order was placed            |
| Pickup_Time              | Time when the agent picked up the order        |
| Weather                  | Weather conditions during delivery             |
| Traffic                  | Traffic conditions during delivery             |
| Vehicle                  | Mode of transport                              |
| Area                     | Type of delivery area (Urban/Metro)            |
| Delivery_Time            | Target variable – actual delivery time (hours) |
| Category                 | Product category                               |

---

## 🔄 Data Flow & Architecture

1. **Data Preparation**: Load → Clean → Feature Engineering → Save processed data
2. **Processing Pipeline**: Preprocess → Train Models → Save models
3. **Model Training**: Train using scikit-learn/XGBoost → Evaluate → Track in MLflow
4. **Deployment**: Streamlit UI for end-user predictions

---

## 📈 Results

By the end of the project, users will have:

* A cleaned, preprocessed dataset ready for modeling
* Multiple regression models trained, evaluated, and tracked via MLflow
* Insights into key factors affecting delivery times
* A functional, user-friendly Streamlit app to predict delivery times

---

## 📏 Project Evaluation Metrics

* **Data Preparation**: Completeness and cleanliness of the dataset
* **Feature Engineering**: Relevance and quality of derived features
* **Model Performance**: Accuracy and reliability (RMSE, MAE, R²)
* **Application Functionality**: Usability and responsiveness of the Streamlit interface
* **Model Tracking**: Accuracy of MLflow logs and model comparisons

---

## 💻 Technical Stack

* **Languages**: Python
* **Libraries**: pandas, numpy, scikit-learn, xgboost, matplotlib, seaborn, MLflow
* **Deployment**: Streamlit
* **Modeling**: Regression modeling and feature engineering

---

## 📦 Deliverables

1. **Source Code**: Python scripts for data prep, EDA, feature engineering, and modeling
2. **Processed Data**: Cleaned dataset ready for analysis
3. **Regression Models**: Trained and evaluated models
4. **Application Code**: Streamlit app with functional predictions
5. **Documentation**: Implementation details and results
6. **Model Tracking**: MLflow logs and model comparisons

---
