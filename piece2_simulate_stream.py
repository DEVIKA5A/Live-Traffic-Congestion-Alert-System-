import pandas as pd
import time

# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv("futuristic_city_traffic.csv")

print("Available columns:")
print(df.columns.tolist())


# ==========================================
# SELECT COLUMNS FROM NEW DATASET
# ==========================================

# Location
location_column = "City"

# Traffic measurement
traffic_column = "Traffic Density"

# Time-related information
hour_column = "Hour Of Day"


# ==========================================
# CHECK REQUIRED COLUMNS
# ==========================================

print("\nDetected columns:")
print("Location column:", location_column)
print("Traffic column:", traffic_column)
print("Hour column:", hour_column)


# ==========================================
# SORT DATA BY HOUR
# ==========================================

if hour_column in df.columns:
    df = df.sort_values(hour_column)


print("\n=================================")
print("STARTING LIVE TRAFFIC SIMULATION")
print("=================================\n")


# ==========================================
# SIMULATE LIVE DATA STREAM
# ==========================================

test_limit = 30

for count, (_, row) in enumerate(df.iterrows()):

    city = row[location_column]
    traffic_density = row[traffic_column]
    hour = row[hour_column]

    print(
        f"[LIVE] "
        f"City: {city} | "
        f"Hour: {hour} | "
        f"Traffic Density: {traffic_density}"
    )

    # Small delay for live simulation
    time.sleep(0.1)

    # Stop after 30 records
    if count >= test_limit - 1:
        break


print("\n=================================")
print("Simulation stopped successfully.")
print("=================================")