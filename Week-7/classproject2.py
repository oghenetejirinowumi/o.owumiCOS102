import pandas as pd

# Organize data as a list of rows instead of uneven columns
data = [
    {"Segment": "Refreshment Beverages", "Brand": "CADBURY BOURNVITA"},
    {"Segment": "Refreshment Beverages", "Brand": "CADBURY 3-in-1 HOT CHOCOLATE"},
    {"Segment": "Confectionery", "Brand": "TOMTOM CLASSIC"},
    {"Segment": "Confectionery", "Brand": "TOMTOM STRAWBERRY"},
    {"Segment": "Confectionery", "Brand": "BUTTERMINT"},
    {"Segment": "Intermediate Cocoa Products", "Brand": "COCOA POWDER"},
    {"Segment": "Intermediate Cocoa Products", "Brand": "COCOA BUTTER"},
]

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('cadburyNigeria_market.csv', index=False)

print("✅ 'cadburyNigeria_market.csv' file has been created successfully.")
