"""
PIECE 3: Traffic Congestion Detection

This program processes the complete futuristic city traffic dataset
and detects congestion using the Traffic Density column.
"""

import pandas as pd

# ==========================================
# LOAD COMPLETE DATASET
# ==========================================

df = pd.read_csv("futuristic_city_traffic.csv")

print("==============================================")
print("DATASET LOADED SUCCESSFULLY")
print("==============================================")

print(f"Total records in dataset: {len(df)}")


# ==========================================
# CONGESTION DETECTION FUNCTION
# ==========================================

def detect_congestion(density):

    density = str(density).upper().strip()

    if density == "SEVERE":
        return "CONGESTED", "SEVERE"

    elif density in ["HIGH", "HEAVY"]:
        return "CONGESTED", "HIGH"

    else:
        return "NORMAL", "NORMAL"


# ==========================================
# PROCESS COMPLETE DATASET
# ==========================================

print("\nProcessing complete dataset...")

results = []

total_records = len(df)

for index, row in df.iterrows():

    # Get dataset values
    city = row["City"]
    vehicle_type = row["Vehicle Type"]
    speed = row["Speed"]
    traffic_density = row["Traffic Density"]

    # Detect congestion
    status, severity = detect_congestion(
        traffic_density
    )

    # Save result
    results.append({

        "City": city,

        "Vehicle Type": vehicle_type,

        "Speed": speed,

        "Traffic Density": traffic_density,

        "Severity": severity,

        "Status": status

    })

    # Show progress every 1000 records
    if (index + 1) % 1000 == 0:

        print(
            f"Processed {index + 1} "
            f"out of {total_records} records"
        )


# ==========================================
# SAVE COMPLETE RESULTS
# ==========================================

results_df = pd.DataFrame(results)

results_df.to_csv(
    "congestion_results.csv",
    index=False
)


# ==========================================
# DISPLAY FINAL SUMMARY
# ==========================================

print("\n==============================================")
print("CONGESTION DETECTION COMPLETED")
print("==============================================")

print(
    f"\nTotal records processed: "
    f"{len(results_df)}"
)

print(
    f"\nCongested records: "
    f"{(results_df['Status'] == 'CONGESTED').sum()}"
)

print(
    f"\nNormal records: "
    f"{(results_df['Status'] == 'NORMAL').sum()}"
)

print("\nTraffic Severity Summary:")

print(
    results_df["Severity"].value_counts()
)

print(
    "\nResults saved successfully to "
    "congestion_results.csv"
)