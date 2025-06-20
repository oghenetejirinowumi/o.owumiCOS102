import pandas as pd
# Load the dataset
data = pd.read_csv("Top-Apps-in-Google-Play.csv")

# Create a DataFrame
df = pd.DataFrame(data)

# 1. Display the first 7 rows
print(df.head(7))

# 2. Select the first 3 columns
first_three_columns = df.iloc[:, :3]
print(first_three_columns.head())  # Just to show a few rows

# 3. Display only one row and the header
print(df.head(1))  # Shows the first row along with column headers


