# Indian-Air-Quality-Monitoring-and-Forecasting

A full-stack data science and machine learning project that analyzes historical Indian air quality data, calculates Air Quality Index (AQI) using standard methodologies, predicts AQI using machine learning models, forecasts future AQI trends using time-series analysis, and deploys the solution as an interactive web application with health recommendations.

---

## 📌 Project Overview

Air pollution is a major environmental and public health concern in India. This project leverages historical air quality data (1990–2015) released by the Central Pollution Control Board (CPCB) and the Ministry of Environment & Forests (MoEF) to build a complete **Air Quality Monitoring, Prediction, and Forecasting System**.

The system:

* Cleans and preprocesses real-world air quality data
* Calculates AQI using **standards-based pollutant breakpoints**
* Predicts AQI from pollutant concentrations using **Machine Learning**
* Forecasts future AQI trends using **ARIMA time-series modeling**
* Classifies air quality levels
* Provides **health recommendations** based on AQI
* Deploys the model as an interactive **Streamlit web application**

---

## 🎯 Objectives

* Analyze historical air pollution trends in India
* Calculate AQI using CPCB-style methodology
* Predict AQI using supervised ML models
* Forecast future AQI values
* Build a user-friendly web application for real-time AQI prediction
* Provide actionable health guidance based on air quality

---

## 🗂 Dataset Description

* **Source:** Central Pollution Control Board (CPCB), MoEF (NDSAP)
* **Time Period:** 1990 – 2015
* **Geographical Scope:** Multiple Indian states and monitoring stations

### Key Features Used

* `so2` – Sulphur Dioxide concentration
* `no2` – Nitrogen Dioxide concentration
* `rspm` – Respirable Suspended Particulate Matter
* `spm` – Suspended Particulate Matter
* `pm2_5` – Fine particulate matter

---

## 🧠 Methodology

### 1️⃣ Data Preprocessing

* Handled non-UTF8 encoding issues
* Converted date columns
* Imputed missing pollutant values using mean imputation

### 2️⃣ Standards-Based AQI Calculation

* Implemented AQI calculation using pollutant breakpoints
* Derived AQI from PM2.5 concentrations

### 3️⃣ Machine Learning (Regression)

* Model Used: **Random Forest Regressor**
* Inputs: SO₂, NO₂, RSPM, SPM, PM2.5
* Output: Predicted AQI value

### 4️⃣ Time-Series Forecasting

* Aggregated AQI values over time
* Used **ARIMA** model to forecast future AQI trends

### 5️⃣ AQI Classification & Health Recommendations

| AQI Range | Category  | Health Advice                       |
| --------- | --------- | ----------------------------------- |
| 0–50      | Good      | Safe for outdoor activities         |
| 51–100    | Moderate  | Sensitive people should be cautious |
| 101–200   | Poor      | Avoid prolonged outdoor exposure    |
| 201–300   | Unhealthy | Wear masks, stay indoors            |
| >300      | Hazardous | Medical attention recommended       |

---

## 🌐 Web Application (Streamlit)

### Features

* User input for pollutant concentrations
* Real-time AQI prediction
* AQI category display
* Health recommendation display

## 🏆 Key Learnings

* Handling real-world datasets with missing values
* Standards-based AQI computation
* End-to-end ML pipeline development
* Time-series forecasting
* Model deployment using Streamlit
