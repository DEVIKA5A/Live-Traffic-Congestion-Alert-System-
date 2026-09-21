import pandas as pd

# Load the new dataset
df = pd.read_csv("futuristic_city_traffic.csv")

# Show basic information
print("First 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nTotal rows:", len(df))

# Show unique cities
if "City" in df.columns:
    print("\nUnique cities:")
    print(df["City"].unique())

# Check for traffic-related columns
print("\nDataset shape (Rows, Columns):")
print(df.shape)