import pandas as pd

# Load dataset
df = pd.read_csv("data/superstore.csv", encoding='latin 1')

# Show first rows
print("\nFirst 5 rows:\n")
print(df.head())

# Show structure
print("\nDataset Info:\n")
print(df.info())

# Show column names
print("\nColumns:\n")
print(df.columns)
