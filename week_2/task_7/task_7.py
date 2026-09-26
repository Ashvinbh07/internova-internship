import pandas as pd

# Read the CSV file
df = pd.read_csv("task7_missing_values.csv")

print("Original Data:")
print(df)

# 1. Detect missing values
print("\n1. Missing Values:")
print(df.isnull())

# 2. Count missing values
print("\n2. Missing Values Count:")
print(df.isnull().sum())

# 3. Remove rows containing missing values
print("\n3. Data After Removing Missing Values:")
df_dropped = df.dropna()
print(df_dropped)

# 4. Fill missing numeric values with the mean
df_filled = df.copy()

df_filled["Age"] = df_filled["Age"].fillna(df_filled["Age"].mean())
df_filled["Marks"] = df_filled["Marks"].fillna(df_filled["Marks"].mean())

# Fill missing categorical value
df_filled["Department"] = df_filled["Department"].fillna("Unknown")

print("\n4. Data After Filling Missing Values:")
print(df_filled)

# 5. Verify missing values
print("\n5. Missing Values After Filling:")
print(df_filled.isnull().sum())