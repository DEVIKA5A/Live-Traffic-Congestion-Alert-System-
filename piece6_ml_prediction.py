"""
PIECE 6: Machine Learning Traffic Prediction

Predicts traffic speed using Random Forest Regression
with the futuristic_city_traffic dataset.
"""

import pandas as pd
import numpy as np
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# =========================================================
# 1. LOAD DATA
# =========================================================

print("\n==========================================")
print("     ML TRAFFIC PREDICTION SYSTEM")
print("==========================================\n")

print("Loading futuristic_city_traffic.csv...")

df = pd.read_csv(
    "futuristic_city_traffic.csv"
)

print("Dataset loaded successfully!")
print("Total records:", len(df))

print("\nAvailable columns:")
print(df.columns.tolist())


# =========================================================
# 2. SELECT REQUIRED COLUMNS
# =========================================================

features = [
    "City",
    "Vehicle Type",
    "Energy Consumption",
    "Traffic Density",
    "Is Peak Hour",
    "Random Event Occurred"
]

target = "Speed"


# =========================================================
# 3. REMOVE MISSING VALUES
# =========================================================

df = df.dropna(
    subset=features + [target]
)

print(
    "\nRecords after cleaning:",
    len(df)
)


# =========================================================
# 4. PREPARE FEATURES
# =========================================================

X = df[features].copy()

# Convert ONLY categorical columns
X = pd.get_dummies(
    X,
    columns=[
        "City",
        "Vehicle Type"
    ],
    dtype=int
)

# Keep numerical columns as numerical values
X["Energy Consumption"] = X[
    "Energy Consumption"
].astype(float)

X["Traffic Density"] = X[
    "Traffic Density"
].astype(float)

X["Is Peak Hour"] = X[
    "Is Peak Hour"
].astype(int)

X["Random Event Occurred"] = X[
    "Random Event Occurred"
].astype(int)


y = df[target].astype(float)


# =========================================================
# 5. TRAIN / TEST SPLIT
# =========================================================

split_index = int(
    len(df) * 0.80
)

X_train = X.iloc[:split_index]

X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]

y_test = y.iloc[split_index:]


print(
    "\nTraining records:",
    len(X_train)
)

print(
    "Testing records :",
    len(X_test)
)


# =========================================================
# 6. CREATE RANDOM FOREST MODEL
# =========================================================

print(
    "\nTraining Random Forest model..."
)

model = RandomForestRegressor(
    n_estimators=100,
    max_depth=15,
    random_state=42,
    n_jobs=-1
)


# =========================================================
# 7. TRAIN MODEL
# =========================================================

model.fit(
    X_train,
    y_train
)

print(
    "Model training completed!"
)


# =========================================================
# 8. MAKE PREDICTIONS
# =========================================================

predictions = model.predict(
    X_test
)


# =========================================================
# 9. EVALUATE MODEL
# =========================================================

mae = mean_absolute_error(
    y_test,
    predictions
)

rmse = np.sqrt(
    mean_squared_error(
        y_test,
        predictions
    )
)

r2 = r2_score(
    y_test,
    predictions
)


print("\n==========================================")
print("        MODEL PERFORMANCE")
print("==========================================")

print(
    "MAE  :",
    round(mae, 2)
)

print(
    "RMSE :",
    round(rmse, 2)
)

print(
    "R²   :",
    round(r2, 4)
)


# =========================================================
# 10. ACTUAL VS PREDICTED RESULTS
# =========================================================

comparison = pd.DataFrame({

    "Actual_Speed":
        y_test.values,

    "Predicted_Speed":
        np.round(
            predictions,
            2
        )
})


print(
    "\nActual vs Predicted Traffic Speed:"
)

print(
    comparison.head(10)
)


# =========================================================
# 11. SAVE MODEL
# =========================================================

joblib.dump(
    model,
    "traffic_prediction_model.pkl"
)

print(
    "\nModel saved as:"
)

print(
    "traffic_prediction_model.pkl"
)


# =========================================================
# 12. SAVE PREDICTION RESULTS
# =========================================================

comparison.to_csv(
    "ml_prediction_results.csv",
    index=False
)

print(
    "\nPrediction results saved as:"
)

print(
    "ml_prediction_results.csv"
)


# =========================================================
# 13. SAMPLE PREDICTION
# =========================================================

sample = X_test.iloc[[0]]

sample_prediction = model.predict(
    sample
)[0]


print("\n==========================================")
print("       SAMPLE TRAFFIC PREDICTION")
print("==========================================")

print(
    "Actual Speed:",
    round(
        y_test.iloc[0],
        2
    )
)

print(
    "Predicted Speed:",
    round(
        sample_prediction,
        2
    )
)


print("\n==========================================")
print("       ML PROCESSING COMPLETED")
print("==========================================")