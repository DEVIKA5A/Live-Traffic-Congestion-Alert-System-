"""
PIECE 5: Apache Spark Processing for
Live Traffic Congestion & Alert System

This program:
1. Loads the complete futuristic city traffic dataset
2. Cleans the data using Apache Spark
3. Processes traffic density information
4. Detects congestion
5. Assigns traffic severity
6. Performs traffic analytics
7. Saves congestion_results.csv for the Streamlit dashboard
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    when,
    upper,
    trim
)

# =========================================================
# 1. CREATE SPARK SESSION
# =========================================================

spark = (
    SparkSession.builder
    .appName("LiveTrafficCongestionSystem")
    .master("local[*]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

print("\n==========================================")
print(" LIVE TRAFFIC CONGESTION & ALERT SYSTEM")
print(" Apache Spark Big Data Processing")
print("==========================================\n")


# =========================================================
# 2. LOAD COMPLETE DATASET
# =========================================================

print("Loading futuristic_city_traffic.csv...\n")

df = spark.read.csv(
    "futuristic_city_traffic.csv",
    header=True,
    inferSchema=True
)

print("Dataset loaded successfully!")

print("\nDataset Schema:")

df.printSchema()

print("\nFirst 5 Records:")

df.show(
    5,
    truncate=False
)


# =========================================================
# 3. DISPLAY TOTAL RECORDS
# =========================================================

total_records = df.count()

print(
    "\nTotal records in dataset:",
    total_records
)


# =========================================================
# 4. DATA CLEANING
# =========================================================

print("\nCleaning dataset...")


# Remove records with missing important values

df = df.dropna(
    subset=[
        "City",
        "Vehicle Type",
        "Speed",
        "Traffic Density"
    ]
)


# Convert Speed to double

df = df.withColumn(
    "Speed",
    col("Speed").cast("double")
)


# Remove invalid speed values

df = df.filter(
    col("Speed") >= 0
)


# Clean Traffic Density text

df = df.withColumn(
    "Traffic Density",
    upper(
        trim(
            col("Traffic Density")
        )
    )
)


print("Data cleaning completed.")


valid_records = df.count()

print(
    "Valid records:",
    valid_records
)


# =========================================================
# 5. DETECT CONGESTION
# =========================================================

print(
    "\nDetecting traffic congestion..."
)


result = df.withColumn(

    "Status",

    when(
        col("Traffic Density").isin(
            "HIGH",
            "HEAVY",
            "SEVERE"
        ),

        "CONGESTED"

    ).otherwise(
        "NORMAL"
    )

)


# =========================================================
# 6. ASSIGN TRAFFIC SEVERITY
# =========================================================

result = result.withColumn(

    "Severity",

    when(
        col("Traffic Density") == "SEVERE",

        "SEVERE"
    )

    .when(
        col("Traffic Density").isin(
            "HIGH",
            "HEAVY"
        ),

        "HIGH"
    )

    .otherwise(
        "NORMAL"
    )

)


# =========================================================
# 7. SELECT FINAL COLUMNS
# =========================================================

result = result.select(

    "City",

    "Vehicle Type",

    "Speed",

    "Traffic Density",

    "Status",

    "Severity"

)


# =========================================================
# 8. DISPLAY SAMPLE RESULTS
# =========================================================

print(
    "\nSample Processed Traffic Results:"
)


result.show(
    20,
    truncate=False
)


# =========================================================
# 9. TRAFFIC ANALYTICS
# =========================================================

total_count = result.count()


congested_count = (
    result
    .filter(
        col("Status")
        == "CONGESTED"
    )
    .count()
)


normal_count = (
    result
    .filter(
        col("Status")
        == "NORMAL"
    )
    .count()
)


print("\n==========================================")
print("          TRAFFIC ANALYTICS")
print("==========================================")

print(
    "Total records     :",
    total_count
)

print(
    "Normal records    :",
    normal_count
)

print(
    "Congested records :",
    congested_count
)


if total_count > 0:

    congestion_rate = (

        congested_count
        / total_count

    ) * 100


    print(

        "Congestion rate   :",

        round(
            congestion_rate,
            2
        ),

        "%"

    )


# =========================================================
# 10. CITY-WISE CONGESTION ANALYSIS
# =========================================================

print(
    "\n=========================================="
)

print(
    "CITY-WISE CONGESTION ANALYSIS"
)

print(
    "=========================================="
)


city_congestion = (

    result

    .filter(
        col("Status")
        == "CONGESTED"
    )

    .groupBy(
        "City"
    )

    .count()

    .orderBy(
        col("count").desc()
    )

)


city_congestion.show(
    20,
    truncate=False
)


# =========================================================
# 11. TRAFFIC DENSITY ANALYSIS
# =========================================================

print(
    "\n=========================================="
)

print(
    "TRAFFIC DENSITY ANALYSIS"
)

print(
    "=========================================="
)


density_analysis = (

    result

    .groupBy(
        "Traffic Density"
    )

    .count()

    .orderBy(
        col("count").desc()
    )

)


density_analysis.show(
    truncate=False
)


# =========================================================
# 12. VEHICLE TYPE ANALYSIS
# =========================================================

print(
    "\n=========================================="
)

print(
    "VEHICLE TYPE ANALYSIS"
)

print(
    "=========================================="
)


vehicle_analysis = (

    result

    .groupBy(
        "Vehicle Type"
    )

    .count()

    .orderBy(
        col("count").desc()
    )

)


vehicle_analysis.show(
    20,
    truncate=False
)


# =========================================================
# 13. SAVE RESULTS
# =========================================================

print(
    "\nSaving processed results..."
)


# Convert to Pandas only for dashboard CSV

result.toPandas().to_csv(

    "congestion_results.csv",

    index=False

)


print(
    "\nResults saved successfully to:"
)

print(
    "congestion_results.csv"
)


# =========================================================
# 14. STOP SPARK
# =========================================================

spark.stop()


print(
    "\n=========================================="
)

print(
    "Spark Big Data Processing Completed!"
)

print(
    "=========================================="
)