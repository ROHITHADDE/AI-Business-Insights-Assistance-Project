# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# ========================
# Load dataset
# ========================
df = pd.read_csv(r"C:\Users\adder\Downloads\Ai DATA\Superstore_with_predictions.csv", encoding="latin1")

# ========================
# Title and Description
# ========================
st.title("📊 Superstore Dashboard with Predictions")
st.markdown("""
This dashboard shows sales, profit, discount trends and predictions for Superstore dataset.
""")

# ========================
# Display Dataset
# ========================
st.subheader("Dataset Preview")
st.dataframe(df)

# ========================
# Key Metrics
# ========================
st.subheader("Key Metrics")
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
avg_discount = df["Discount"].mean()
total_quantity = df["Quantity"].sum()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Average Discount", f"{avg_discount:.2%}")
col4.metric("Total Quantity Sold", f"{total_quantity}")

# ========================
# Sales by Category
# ========================
st.subheader("Sales by Category")
sales_category = df.groupby("Category")["Sales"].sum().reset_index()
fig1 = px.bar(sales_category, x="Category", y="Sales", color="Category", text="Sales")
st.plotly_chart(fig1)

# ========================
# Profit by Sub-Category
# ========================
st.subheader("Profit by Sub-Category")
profit_subcat = df.groupby("Sub-Category")["Profit"].sum().reset_index()
fig2 = px.bar(profit_subcat, x="Sub-Category", y="Profit", color="Profit", text="Profit")
st.plotly_chart(fig2)

# ========================
# Discount vs Profit
# ========================
st.subheader("Discount vs Profit")
fig3 = px.scatter(df, x="Discount", y="Profit", color="Category", size="Sales",
                  hover_data=["Product Name"])
st.plotly_chart(fig3)

# ========================
# Predictions Visualization
# ========================
# Make sure your dataset has a column named 'Predicted_Sales' or similar
if "Predicted_Sales" in df.columns:
    st.subheader("Sales vs Predicted Sales")
    fig4 = px.scatter(df, x="Sales", y="Predicted_Sales", color="Category",
                      hover_data=["Product Name"])
    st.plotly_chart(fig4)
else:
    st.info("No 'Predicted_Sales' column found in dataset for prediction visualization.")

# ========================
# Filter by Region
# ========================
st.subheader("Filter by Region")
regions = df["Region"].unique()
selected_region = st.selectbox("Select Region", regions)
filtered_data = df[df["Region"] == selected_region]
st.write(f"Showing data for region: {selected_region}")
st.dataframe(filtered_data.head())
