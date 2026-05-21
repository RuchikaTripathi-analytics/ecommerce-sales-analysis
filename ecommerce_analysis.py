import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv("ecommerce_sales.csv")

print("\n📊 FULL DATASET")
print(df)

# ---------------- TOTAL SALES ----------------
print("\n💰 TOTAL SALES:")
print(df["Sales"].sum())

# ---------------- SALES BY PRODUCT ----------------
product_sales = df.groupby("Product")["Sales"].sum()

print("\n🏆 SALES BY PRODUCT:")
print(product_sales)

# ---------------- SALES BY CITY ----------------
city_sales = df.groupby("City")["Sales"].sum()

print("\n🏙️ SALES BY CITY:")
print(city_sales)

# ---------------- BAR CHART ----------------
plt.figure(figsize=(7,5))

product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show()

# ---------------- PIE CHART ----------------
plt.figure(figsize=(6,6))

city_sales.plot(kind="pie", autopct="%1.1f%%")

plt.title("Sales by City")

plt.ylabel("")

plt.show()

# ---------------- BUSINESS INSIGHTS ----------------

print("\n📌 BUSINESS INSIGHTS")

top_product = df.groupby("Product")["Sales"].sum().idxmax()
top_city = df.groupby("City")["Sales"].sum().idxmax()

print(f"\n🏆 Top Selling Product: {top_product}")

print(f"\n🌆 City With Highest Sales: {top_city}")

print("\n✅ Electronics category is generating strong revenue.")