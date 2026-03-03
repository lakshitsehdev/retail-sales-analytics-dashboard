import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Superstore Sales Dashboard")

# Load data
df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

df["Order Year"] = df["Order Date"].dt.year
df["Delivery Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

# KPI Section
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${df['Sales'].sum():,.0f}")
col2.metric("Total Profit", f"${df['Profit'].sum():,.0f}")
col3.metric("Avg Delivery Days", f"{df['Delivery Days'].mean():.2f}")

# Sales by Category
st.subheader("Sales by Category")

category_sales = df.groupby("Category")["Sales"].sum()

fig1 = plt.figure()
category_sales.plot(kind="bar")
plt.ylabel("Sales")
st.pyplot(fig1)

# Discount vs Profit
st.subheader("Discount vs Profit")

fig2 = plt.figure()
sns.scatterplot(x="Discount", y="Profit", data=df)
st.pyplot(fig2)

# Yearly Sales Trend
st.subheader("Yearly Sales Trend")

yearly_sales = df.groupby("Order Year")["Sales"].sum()

fig3 = plt.figure()
yearly_sales.plot(kind="line")
plt.ylabel("Sales")
st.pyplot(fig3)