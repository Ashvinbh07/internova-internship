import pandas as pd


# Read CSV files
customers = pd.read_csv("task8_customers.csv")
orders = pd.read_csv("task8_orders.csv")
january = pd.read_csv("task8_sales_january.csv")
february = pd.read_csv("task8_sales_february.csv")


print("Customers Data:")
print(customers)

print("\nOrders Data:")
print(orders)

print("\nJanuary Sales:")
print(january)

print("\nFebruary Sales:")
print(february)


# 1. Concatenate January and February sales
combined_sales = pd.concat(
    [january, february],
    ignore_index=True
)

print("\n1. Combined January and February Sales:")
print(combined_sales)


# 2. Merge customers and orders
merged_data = pd.merge(
    orders,
    customers,
    on="Customer_ID",
    how="inner"
)

print("\n2. Merged Customer and Order Data:")
print(merged_data)


# 3. GroupBy - Total sales by category
category_sales = orders.groupby("Category")["Sales"].sum()

print("\n3. Total Sales by Category:")
print(category_sales)


# 4. GroupBy with multiple statistics
category_summary = orders.groupby("Category")["Sales"].agg(
    ["sum", "mean", "count"]
)

print("\n4. Category Sales Summary:")
print(category_summary)


# 5. Pivot Table
pivot = pd.pivot_table(
    merged_data,
    values="Sales",
    index="City",
    columns="Category",
    aggfunc="sum",
    fill_value=0
)

print("\n5. Pivot Table - Sales by City and Category:")
print(pivot)