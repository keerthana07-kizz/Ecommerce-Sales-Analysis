import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("E-Commerce Sales Data Analysis")

# Load the dataset
df = pd.read_csv("ecommerce_sales.csv")

# Display first 5 rows
print(df.head())

# Understand the dataset
print("\nShape of the dataset:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nDataset information:")
print(df.info())

print("\nStatistical summary:")
print(df.describe())

print("\nMissing values:")
print(df.isnull().sum())


# Calculate Total Sales
df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

print("\nData with Total Sales:")
print(df.head())


# Calculate Total Revenue
total_revenue = df["Total_Sales"].sum()

print("\nTotal Revenue:")
print(total_revenue)


# Sales by Product
product_sales = df.groupby("Product")["Total_Sales"].sum()

print("\nSales by Product:")
print(product_sales.sort_values(ascending=False))
# Sales by Category
category_sales = df.groupby("Category")["Total_Sales"].sum()

print("\nSales by Category:")
print(category_sales.sort_values(ascending=False))
# Sales by City
city_sales = df.groupby("City")["Total_Sales"].sum()

print("\nSales by City:")
print(city_sales.sort_values(ascending=False))
# Convert Order_Date to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Create Month column
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

# Sales by Month
monthly_sales = df.groupby("Month")["Total_Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)
# Product Sales Chart
product_sales.sort_values(ascending=False).plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()
# Category Sales Chart
category_sales.sort_values(ascending=False).plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()
# City Sales Chart
city_sales.sort_values(ascending=False).plot(kind="bar")

plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()
# Monthly Sales Chart
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Sales by Payment Method
payment_sales = df.groupby("Payment_Method")["Total_Sales"].sum()

print("\nSales by Payment Method:")
print(payment_sales.sort_values(ascending=False))
# Sales by Customer
customer_sales = df.groupby("Customer_Name")["Total_Sales"].sum()

print("\nSales by Customer:")
print(customer_sales.sort_values(ascending=False))
# Quantity Sold by Product
product_quantity = df.groupby("Product")["Quantity"].sum()

print("\nQuantity Sold by Product:")
print(product_quantity.sort_values(ascending=False))
# Average Order Value
average_order_value = df["Total_Sales"].mean()

print("\nAverage Order Value:")
print(average_order_value)
# Top 5 Products
top_products = product_sales.sort_values(ascending=False).head(5)

print("\nTop 5 Products by Sales:")
print(top_products)
# Top 5 Cities
top_cities = city_sales.sort_values(ascending=False).head(5)

print("\nTop 5 Cities by Sales:")
print(top_cities)
# Highest Revenue Order
highest_order = df.loc[df["Total_Sales"].idxmax()]

print("\nHighest Revenue Order:")
print(highest_order)
# Payment Method Sales Chart
payment_sales.sort_values(ascending=False).plot(kind="bar")

plt.title("Sales by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()
# Monthly Sales Bar Chart
monthly_sales.plot(kind="bar")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()
# Category Sales Pie Chart
category_sales.plot(kind="pie", autopct="%1.1f%%")

plt.title("Sales Distribution by Category")
plt.ylabel("")

plt.tight_layout()
plt.show()
# Sales Statistics
minimum_sale = df["Total_Sales"].min()
maximum_sale = df["Total_Sales"].max()
average_sale = df["Total_Sales"].mean()

print("\nSales Statistics:")
print("Minimum Sale:", minimum_sale)
print("Maximum Sale:", maximum_sale)
print("Average Sale:", average_sale)
# Total Quantity Sold
total_quantity = df["Quantity"].sum()

print("\nTotal Quantity Sold:")
print(total_quantity)
# Number of Orders
total_orders = df["Order_ID"].nunique()

print("\nTotal Number of Orders:")
print(total_orders)