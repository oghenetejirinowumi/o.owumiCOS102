import pandas as pd

# Load the dataset
data = pd.read_csv("BTC_DATA_V3.0.csv")

df = pd.DataFrame(data)

# Task 1: Display the first 7 rows
print("First 7 rows of the dataset:")
print(df.head(7))

# Task 2: Select and display the first 3 columns
print("\nFirst 3 columns of the dataset:")
first_three_columns = df.iloc[:, :3]
print(first_three_columns.head())

# Task 3: Display only one row (first row) with the header
print("\nFirst row with column headers:")
print(df.head(1))

