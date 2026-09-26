import pandas as pd
import numpy as np

df = pd.read_csv("sales_dataset.csv")


# Data Inspection


print("DATASET SHAPE:")
print(df.shape)

print("\nFIRST 5 ROWS:")
print(df.head())

print("\nLAST 5 ROWS:")
print(df.tail())

print("\nCOLUMN NAMES:")
print(df.columns.tolist())

print("\nDATA TYPES:")
print(df.dtypes)

print("\nDATASET INFO:")
df.info()

print("\nSTATISTICAL SUMMARY:")
print(df.describe())

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())


# DATA CLEANING


print("\nDATA CLEANING:")

# Create a copy of the original dataset
cleaned_df = df.copy()


# 1. Remove duplicate rows


print("\nDuplicate rows before cleaning:")
print(cleaned_df.duplicated().sum())

cleaned_df = cleaned_df.drop_duplicates()

print("Duplicate rows after cleaning:")
print(cleaned_df.duplicated().sum())


# 2. Convert Order_Date to datetime


cleaned_df["Order_Date"] = pd.to_datetime(
    cleaned_df["Order_Date"],
    errors="coerce"
)

print("\nOrder_Date data type:")
print(cleaned_df["Order_Date"].dtype)



# 3. Clean text columns


text_columns = [
    "Customer_Name",
    "Product",
    "Category",
    "Subcategory",
    "City",
    "Region",
    "Customer_Segment",
    "Payment_Method",
    "Order_Status",
    "Sales_Channel"
]

for column in text_columns:
    cleaned_df[column] = cleaned_df[column].str.strip()


# Standardize category names
cleaned_df["Category"] = cleaned_df["Category"].str.title()

# Standardize city names
cleaned_df["City"] = cleaned_df["City"].str.title()

# Correct Bangalore variation
cleaned_df["City"] = cleaned_df["City"].replace(
    {"Bangalore": "Bengaluru"}
)


# 4. Handle missing values


print("\nMissing values before filling:")
print(cleaned_df.isnull().sum()[cleaned_df.isnull().sum() > 0])


# Fill missing customer names
cleaned_df["Customer_Name"] = cleaned_df["Customer_Name"].fillna(
    "Unknown Customer"
)

# Fill missing city
cleaned_df["City"] = cleaned_df["City"].fillna(
    "Unknown"
)

# Fill missing payment method
cleaned_df["Payment_Method"] = cleaned_df["Payment_Method"].fillna(
    "Unknown"
)

# Fill missing discount with median
cleaned_df["Discount"] = cleaned_df["Discount"].fillna(
    cleaned_df["Discount"].median()
)

# Fill missing profit with median
cleaned_df["Profit"] = cleaned_df["Profit"].fillna(
    cleaned_df["Profit"].median()
)


# 5. Handle invalid Quantity values


print("\nInvalid Quantity values:")
print((cleaned_df["Quantity"] <= 0).sum())

# Replace invalid quantities with NaN
cleaned_df.loc[
    cleaned_df["Quantity"] <= 0,
    "Quantity"
] = np.nan

# Fill invalid quantity values with median
cleaned_df["Quantity"] = cleaned_df["Quantity"].fillna(
    cleaned_df["Quantity"].median()
)

# Convert quantity back to integer
cleaned_df["Quantity"] = cleaned_df["Quantity"].astype(int)


# 6. Handle invalid Discount values


print("\nInvalid Discount values:")
print(
    (
        (cleaned_df["Discount"] < 0) |
        (cleaned_df["Discount"] > 0.50)
    ).sum()
)

# Replace unrealistic discounts with median
median_discount = cleaned_df["Discount"].median()

cleaned_df.loc[
    (cleaned_df["Discount"] < 0) |
    (cleaned_df["Discount"] > 0.50),
    "Discount"
] = median_discount


# 7. Final missing-value check


print("\nMissing values after cleaning:")
print(cleaned_df.isnull().sum())


# 8. Final dataset information


print("\nCLEANED DATASET")

print("Rows:", len(cleaned_df))
print("Columns:", len(cleaned_df.columns))

print("\nFirst 5 cleaned rows:")
print(cleaned_df.head())

print("\nData types after cleaning:")
print(cleaned_df.dtypes)


# FILTERING AND SORTING


print("\nFILTERING AND SORTING:")


# 1. Select specific columns


print("\nSelected columns:")
print(
    cleaned_df[
        ["Order_ID", "Product", "Category", "Sales", "Profit"]
    ].head(10)
)


# 2. Select specific rows


print("\nFirst 10 rows:")
print(cleaned_df.iloc[:10])


# 3. Filter high-value sales


high_sales = cleaned_df[cleaned_df["Sales"] > 50000]

print("\nOrders with Sales greater than 50,000:")
print(high_sales[
    ["Order_ID", "Product", "Sales", "Profit"]
].head(10))


# 4. Multiple filtering conditions


high_profit_electronics = cleaned_df[
    (cleaned_df["Category"] == "Electronics") &
    (cleaned_df["Profit"] > 5000)
]

print("\nElectronics orders with Profit greater than 5,000:")
print(
    high_profit_electronics[
        ["Product", "Category", "Sales", "Profit"]
    ].head(10)
)


# 5. Sort by Sales - Descending


top_sales = cleaned_df.sort_values(
    by="Sales",
    ascending=False
)

print("\nTop 10 orders by Sales:")
print(
    top_sales[
        ["Order_ID", "Product", "Sales", "Profit"]
    ].head(10)
)



# 6. Sort by Profit - Ascending


lowest_profit = cleaned_df.sort_values(
    by="Profit",
    ascending=True
)

print("\n10 orders with lowest Profit:")
print(
    lowest_profit[
        ["Order_ID", "Product", "Sales", "Profit"]
    ].head(10)
)



# NUMPY ANALYSIS


print("\nNUMPY ANALYSIS:")

sales_array = cleaned_df["Sales"].to_numpy()
profit_array = cleaned_df["Profit"].to_numpy()
quantity_array = cleaned_df["Quantity"].to_numpy()


# 1. Sales statistics


print("\nSales Statistics:")

print("Total Sales:", np.sum(sales_array))
print("Average Sales:", np.mean(sales_array))
print("Median Sales:", np.median(sales_array))
print("Minimum Sales:", np.min(sales_array))
print("Maximum Sales:", np.max(sales_array))
print("Standard Deviation:", np.std(sales_array))


# 2. Profit statistics


print("\nProfit Statistics:")

print("Total Profit:", np.sum(profit_array))
print("Average Profit:", np.mean(profit_array))
print("Median Profit:", np.median(profit_array))
print("Minimum Profit:", np.min(profit_array))
print("Maximum Profit:", np.max(profit_array))
print("Standard Deviation:", np.std(profit_array))


# 3. Quantity statistics


print("\nQuantity Statistics:")

print("Total Quantity:", np.sum(quantity_array))
print("Average Quantity:", np.mean(quantity_array))
print("Minimum Quantity:", np.min(quantity_array))
print("Maximum Quantity:", np.max(quantity_array))


# GROUPBY ANALYSIS


print("\nGROUPBY ANALYSIS:")


# 1. Sales and Profit by Category


category_analysis = (
    cleaned_df
    .groupby("Category")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Average_Sales=("Sales", "mean"),
        Order_Count=("Order_ID", "count")
    )
    .sort_values("Total_Sales", ascending=False)
)

print("\nSales and Profit by Category:")
print(category_analysis)


# 2. Sales and Profit by Region


region_analysis = (
    cleaned_df
    .groupby("Region")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Order_Count=("Order_ID", "count")
    )
    .sort_values("Total_Sales", ascending=False)
)

print("\nSales and Profit by Region:")
print(region_analysis)


# 3. Sales by Customer Segment


segment_analysis = (
    cleaned_df
    .groupby("Customer_Segment")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Order_Count=("Order_ID", "count")
    )
    .sort_values("Total_Sales", ascending=False)
)

print("\nSales by Customer Segment:")
print(segment_analysis)


# 4. Product Performance


product_analysis = (
    cleaned_df
    .groupby("Product")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Quantity_Sold=("Quantity", "sum"),
        Order_Count=("Order_ID", "count")
    )
    .sort_values("Total_Sales", ascending=False)
)

print("\nTop 10 Products by Sales:")
print(product_analysis.head(10))


# 5. Monthly Sales Analysis


cleaned_df["Month"] = cleaned_df["Order_Date"].dt.to_period("M")

monthly_sales = (
    cleaned_df
    .groupby("Month")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Order_Count=("Order_ID", "count")
    )
    .sort_index()
)

print("\nMonthly Sales:")
print(monthly_sales)


# PIVOT TABLE ANALYSIS

print("\nPIVOT TABLE ANALYSIS:")


# 1. Category vs Region - Sales


category_region_pivot = pd.pivot_table(
    cleaned_df,
    values="Sales",
    index="Category",
    columns="Region",
    aggfunc="sum",
    fill_value=0
)

print("\nSales by Category and Region:")
print(category_region_pivot)


# 2. Customer Segment vs Category


segment_category_pivot = pd.pivot_table(
    cleaned_df,
    values="Sales",
    index="Customer_Segment",
    columns="Category",
    aggfunc="sum",
    fill_value=0
)

print("\nSales by Customer Segment and Category:")
print(segment_category_pivot)


# 3. Region vs Order Status


region_status_pivot = pd.pivot_table(
    cleaned_df,
    values="Sales",
    index="Region",
    columns="Order_Status",
    aggfunc="sum",
    fill_value=0
)

print("\nSales by Region and Order Status:")
print(region_status_pivot)


# BUSINESS INSIGHTS


print("\nBUSINESS INSIGHTS:")


# 1. Highest Sales Category


highest_category = category_analysis["Total_Sales"].idxmax()
highest_category_sales = category_analysis.loc[
    highest_category, "Total_Sales"
]

print("\n1. Highest Sales Category:")
print(highest_category)
print("Sales:", round(highest_category_sales, 2))


# 2. Highest Profit Category


highest_profit_category = category_analysis["Total_Profit"].idxmax()
highest_category_profit = category_analysis.loc[
    highest_profit_category, "Total_Profit"
]

print("\n2. Highest Profit Category:")
print(highest_profit_category)
print("Profit:", round(highest_category_profit, 2))


# 3. Highest Sales Region


highest_region = region_analysis["Total_Sales"].idxmax()
highest_region_sales = region_analysis.loc[
    highest_region, "Total_Sales"
]

print("\n3. Highest Sales Region:")
print(highest_region)
print("Sales:", round(highest_region_sales, 2))


# 4. Highest Sales Customer Segment


highest_segment = segment_analysis["Total_Sales"].idxmax()
highest_segment_sales = segment_analysis.loc[
    highest_segment, "Total_Sales"
]

print("\n4. Highest Sales Customer Segment:")
print(highest_segment)
print("Sales:", round(highest_segment_sales, 2))


# 5. Top Product


top_product = product_analysis["Total_Sales"].idxmax()
top_product_sales = product_analysis.loc[
    top_product, "Total_Sales"
]

print("\n5. Top Product by Sales:")
print(top_product)
print("Sales:", round(top_product_sales, 2))


# 6. Most Profitable Product


top_profit_product = product_analysis["Total_Profit"].idxmax()
top_product_profit = product_analysis.loc[
    top_profit_product, "Total_Profit"
]

print("\n6. Most Profitable Product:")
print(top_profit_product)
print("Profit:", round(top_product_profit, 2))


# 7. Best Sales Month


best_month = monthly_sales["Total_Sales"].idxmax()
best_month_sales = monthly_sales.loc[
    best_month, "Total_Sales"
]

print("\n7. Best Sales Month:")
print(best_month)
print("Sales:", round(best_month_sales, 2))


# 8. Lowest Sales Month


lowest_month = monthly_sales["Total_Sales"].idxmin()
lowest_month_sales = monthly_sales.loc[
    lowest_month, "Total_Sales"
]

print("\n8. Lowest Sales Month:")
print(lowest_month)
print("Sales:", round(lowest_month_sales, 2))


# 9. Order Status Analysis


status_analysis = (
    cleaned_df
    .groupby("Order_Status")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Order_Count=("Order_ID", "count")
    )
    .sort_values("Total_Sales", ascending=False)
)

print("\n9. Sales by Order Status:")
print(status_analysis)


# 10. Sales Channel Analysis


channel_analysis = (
    cleaned_df
    .groupby("Sales_Channel")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Order_Count=("Order_ID", "count")
    )
    .sort_values("Total_Sales", ascending=False)
)

print("\n10. Sales by Sales Channel:")
print(channel_analysis)


# EXPORT CLEANED DATASET


print("\nEXPORTING DATASET:")

# Remove helper column before exporting
final_df = cleaned_df.copy()

# Convert Month back to string if it exists
if "Month" in final_df.columns:
    final_df["Month"] = final_df["Month"].astype(str)

# Export
output_file = "cleaned_sales_dataset.csv"

final_df.to_csv(
    output_file,
    index=False
)

print("\nCleaned dataset exported successfully.")
print("File:", output_file)


# Verify exported file


exported_df = pd.read_csv(output_file)

print("\nExported dataset shape:")
print(exported_df.shape)

print("\nFirst 5 rows of exported dataset:")
print(exported_df.head())

print("\nExport verification successful.")