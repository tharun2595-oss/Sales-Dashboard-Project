import pandas as pd

# Load data
df = pd.read_csv("data/superstore.csv", encoding='latin1')

# 1. Remove duplicate rows
df.drop_duplicates(inplace=True)

# 2. Convert date column
df['Order Date'] = pd.to_datetime(df['Order Date'])

# 3. Fix column names (remove spaces)
df.columns = df.columns.str.strip().str.replace(' ', '_')

# 4. Check missing values
print("\nMissing Values:\n")
print(df.isnull().sum())

# 5. Convert numeric columns if needed
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')

# 6. Drop rows with missing important values
df.dropna(subset=['Sales', 'Profit'], inplace=True)

# Save cleaned data
df.to_csv("outputs/cleaned_data.csv", index=False)

print("\nData cleaned and saved successfully ")
