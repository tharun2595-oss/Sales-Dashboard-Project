import streamlit as st
import pandas as pd
import os

# Load data

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR,"outputs", "cleaned_data.csv")
df = pd.read_csv(file_path)

# Title
st.title("📊 Sales Dashboard")

# KPI Metrics
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()

st.metric("Total Sales", f"{total_sales:,.0f}")
st.metric("Total Profit", f"{total_profit:,.0f}")

# Sales by Region
st.subheader("Sales by Region")
region_sales = df.groupby('Region')['Sales'].sum()
st.bar_chart(region_sales)

# Monthly Sales Trend
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Month'] = df['Order_Date'].dt.to_period('M')

monthly_sales = df.groupby('Month')['Sales'].sum()
st.line_chart(monthly_sales)

# Category Profit
st.subheader("Profit by Category")
category_profit = df.groupby('Category')['Profit'].sum()
st.bar_chart(category_profit)

# region filter

region = st.selectbox("Select Region", df['Region'].unique())
filtered_df = df[df['Region'] == region]

st.bar_chart(filtered_df.groupby('Category')['Sales'].sum())
