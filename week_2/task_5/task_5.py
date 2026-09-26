import pandas as pd

#Read the CSV file
df = pd.read_csv("sales_data.csv")

#Display the first 5 rows
print("First 5 Rows:")
print(df.head())

#Display the last 5 rows
print("\nLast 5 Rows:")
print(df.tail())

#Check the number of rows and columns
print("\nNumber of Rows and Columns:")
print(df.shape)

print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

#Display column names
print("\nColumn Names:")
print(df.columns)

#Check data types
print("\nData Types:")
print(df.dtypes)

#Display DataFrame information
print("\nDataFrame Information:")
df.info()

#Display statistical summary
print("\nStatistical Summary:")
print(df.describe())