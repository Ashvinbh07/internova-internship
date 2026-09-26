import pandas as pd

# Read the monthly sales files
january = pd.read_csv("../task_8/task8_sales_january.csv")
february = pd.read_csv("../task_8/task8_sales_february.csv")

# Combine January and February data
combined_sales = pd.concat(
    [january, february],
    ignore_index=True
)

print("Combined Sales Data:")
print(combined_sales)


# 1. Export DataFrame to CSV
combined_sales.to_csv(
    "task9_combined_sales.csv",
    index=False
)

print("\n1. CSV file exported successfully.")


# 2. Export DataFrame to Excel
combined_sales.to_excel(
    "task9_combined_sales.xlsx",
    index=False
)

print("2. Excel file exported successfully.")


# 3. Verify exported data
csv_data = pd.read_csv("task9_combined_sales.csv")

print("\n3. Data Read Back from Exported CSV:")
print(csv_data)