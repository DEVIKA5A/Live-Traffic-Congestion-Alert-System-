# Live Traffic Congestion & Alert System

## 📌 Project Overview

The **Live Traffic Congestion & Alert System** is a Big Data and Machine Learning based project designed to monitor traffic conditions, detect congestion, generate alerts, and predict traffic speed.

The system processes a large traffic dataset using **Apache Spark**, performs congestion analysis, and uses a **Random Forest Regression** model for traffic speed prediction. A **Streamlit dashboard** is used to visualize traffic information and alerts.

---

## 🎯 Objectives

- Process a large traffic dataset efficiently.
- Clean and analyze traffic data using Apache Spark.
- Detect traffic congestion automatically.
- Identify traffic severity levels.
- Generate alerts for congested traffic.
- Predict traffic speed using Machine Learning.
- Display traffic analytics through an interactive Streamlit dashboard.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **Apache PySpark**
- **Scikit-learn**
- **Random Forest Regression**
- **Joblib**
- **Streamlit**
- **Matplotlib / Plotly**
- **Git & GitHub**

---

## 📂 Project Structure

```text
Live-Traffic-Congestion-Alert-System/
│
├── piece1_load.py
├── piece2_simulate_stream.py
├── piece3_detect_congestion.py
├── piece4_dashboard.py
├── piece5_spark_processing.py
├── piece6_ml_prediction.py
│
└── README.md


---

📊 Dataset

The project uses:

Dataset: futuristic_city_traffic.csv

The dataset contains approximately 1.2 million traffic records and includes information such as:

City

Vehicle Type

Weather

Economic Condition

Day Of Week

Hour Of Day

Speed

Is Peak Hour

Random Event Occurred

Energy Consumption

Traffic Density


Dataset Availability

The dataset is not included in this GitHub repository because of its large file size.

Place the following file in the project folder before running the programs:

futuristic_city_traffic.csv


---

🔄 Project Workflow

futuristic_city_traffic.csv
          ↓
   Load & Inspect Data
          ↓
   Live Traffic Simulation
          ↓
 Apache Spark Processing
          ↓
      Data Cleaning
          ↓
   Traffic Analysis
          ↓
 Congestion Detection
          ↓
   Severity Detection
          ↓
     Alert Generation
          ↓
   Machine Learning
          ↓
 Random Forest Regression
          ↓
  Traffic Speed Prediction
          ↓
   Streamlit Dashboard


---

🧩 Project Modules

1. Data Loading and Inspection

File: piece1_load.py

This program:

Loads the traffic dataset.

Displays the first few records.

Displays column names.

Displays data types.

Shows the number of records.

Displays available cities.

Shows the dataset shape.



---

2. Live Traffic Simulation

File: piece2_simulate_stream.py

This module simulates a live traffic data stream using records from the historical dataset.

It displays:

City

Hour

Traffic Density


The simulation is used for demonstration purposes.


---

3. Traffic Congestion Detection

File: piece3_detect_congestion.py

This module processes the traffic data and detects congestion.

Traffic density information is used to determine:

Normal traffic

High congestion

Severe congestion


The processed results are saved as:

congestion_results.csv


---

4. Streamlit Dashboard

File: piece4_dashboard.py

The Streamlit dashboard provides an interactive interface for monitoring traffic.

It displays:

Total traffic records

Congested records

Normal records

Congestion rate

City-wise traffic information

Vehicle type distribution

Traffic density analysis

Speed analysis

Traffic alerts

Machine Learning prediction results



---

5. Apache Spark Big Data Processing

File: piece5_spark_processing.py

Apache Spark is used to process the large traffic dataset.

The module performs:

Dataset loading

Data cleaning

Missing-value handling

Speed validation

Traffic density processing

Congestion detection

Severity classification

City-wise analysis

Vehicle-type analysis


The processed results are saved for dashboard visualization.


---

6. Machine Learning Traffic Prediction

File: piece6_ml_prediction.py

A Random Forest Regression model is used to predict traffic speed.

Features

The model uses traffic-related features such as:

City

Vehicle Type

Energy Consumption

Traffic Density

Is Peak Hour

Random Event Occurred


Target

Speed

Model

Random Forest Regressor

The dataset is divided into:

80% → Training
20% → Testing

Evaluation Metrics

The model is evaluated using:

Mean Absolute Error (MAE)

Root Mean Squared Error (RMSE)

R² Score


The trained model is saved as:

traffic_prediction_model.pkl


---

🚨 Alert System

When traffic congestion is detected, the system generates an alert containing information such as:

City

Vehicle Type

Speed

Traffic Density

Severity

Congestion Status


Alerts can be recorded in:

alerts.csv


---

▶️ How to Run the Project

Step 1: Install Python Dependencies

pip install pandas numpy scikit-learn joblib pyspark streamlit

Step 2: Place Dataset

Place:

futuristic_city_traffic.csv

in the same folder as the Python files.

Step 3: Load and Inspect Dataset

python piece1_load.py

Step 4: Simulate Live Traffic

python piece2_simulate_stream.py

Step 5: Detect Congestion

python piece3_detect_congestion.py

Step 6: Run Spark Processing

python piece5_spark_processing.py

Step 7: Train Machine Learning Model

python piece6_ml_prediction.py

Step 8: Start Streamlit Dashboard

streamlit run piece4_dashboard.py

The dashboard will open in the browser.


---

📈 Expected Outputs

The system produces:

congestion_results.csv
ml_prediction_results.csv
traffic_prediction_model.pkl
alerts.csv

These files are generated during project execution and are not required to be stored in the source-code repository.


---

💡 Advantages

Handles large-scale traffic data.

Uses Apache Spark for Big Data processing.

Provides automated congestion detection.

Generates traffic alerts.

Uses Machine Learning for speed prediction.

Provides an interactive dashboard.

Can be extended to real-time traffic sensor or API data.



---

🔮 Future Enhancements

Connect the system to real-time traffic sensors.

Integrate live traffic APIs.

Deploy Spark on a distributed cluster.

Add GPS-based traffic monitoring.

Improve prediction using advanced Machine Learning models.

Add map-based traffic visualization.

Send real-time notifications to users.



