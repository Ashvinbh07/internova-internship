import pandas as pd

#Read the dataset
df = pd.read_csv("sales_data.csv")

print("Original Data:")
print(df)


#Selecting Specific Columns
print("\n1. Selected Columns - Product and Sales:")
selected_columns = df[["Product", "Sales"]]
print(selected_columns)


#Selecting Specific Rows
print("\n2. Selected Rows - First 3 Rows:")
selected_rows = df.iloc[0:3]
print(selected_rows)


#Filtering Using One Condition
print("\n3. Products with Sales Greater Than 20000:")
filtered_data = df[df["Sales"] > 20000]
print(filtered_data)


#Filtering Using Multiple Conditions
print("\n4. Electronics Products with Sales Greater Than 10000:")
multiple_filter = df[
    (df["Category"] == "Electronics") &
    (df["Sales"] > 10000)
]
print(multiple_filter)


#Sorting in Ascending Order
print("\n5. Data Sorted by Sales - Ascending:")
ascending_data = df.sort_values(by="Sales", ascending=True)
print(ascending_data)


#Sorting in Descending Order
print("\n6. Data Sorted by Sales - Descending:")
descending_data = df.sort_values(by="Sales", ascending=False)
print(descending_data)