import pandas as pd

# Load cleaned data
df = pd.read_csv("outputs/cleaned_data.csv")

# 1. Total Sales
total_sales = df['Sales'].sum()
print("\nTotal Sales:", total_sales)

# 2. Sales by Region
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print("\nSales by Region:\n", region_sales)

# 3. Top 10 Products
top_products = df.groupby('Product_Name')['Sales'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products:\n", top_products)

# 4. Monthly Sales Trend
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Month'] = df['Order_Date'].dt.to_period('M')

monthly_sales = df.groupby('Month')['Sales'].sum()
print("\nMonthly Sales Trend:\n", monthly_sales)

# 5. Profit by Category
category_profit = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)
print("\nProfit by Category:\n", category_profit)
