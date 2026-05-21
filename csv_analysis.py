import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("sales_data.csv")

print("\n📊 FULL DATA")
print(df)

# ---------------- SALES BY PRODUCT ----------------
product_sales = df.groupby("Product")["Sales"].sum()

plt.figure(figsize=(6,4))
product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show()

# ---------------- SALES BY CITY ----------------
city_sales = df.groupby("City")["Sales"].sum()

plt.figure(figsize=(6,4))
city_sales.plot(kind="pie", autopct="%1.1f%%")

plt.title("Sales by City")

plt.ylabel("")

plt.show(block=True)