import pandas as pd 

data = pd.read_csv("programming language trend over time.csv")

df = pd.DataFrame(data)

# Display the first 7 rowms
print("\nThe First 7 Rows of the Dataset:")
print(df.head(7))

# Select and display the first 3 columns
print("\nThe First 3 columns of the Dataset:")
first_three_columns = df.iloc[:, :3]
print(first_three_columns)

# Display only one row (first row) with the header
print("\nThe First Row wit2h Column Headers:")
print(df.head(1))
