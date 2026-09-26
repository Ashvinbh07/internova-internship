import pandas as pd


# Pandas Series
marks = pd.Series([85, 90, 78, 92, 88])

print("Pandas Series:")
print(marks)


# Student Information
students = {
    "Name": ["Rahul", "Priya", "Amit", "Neha", "Rohan"],
    "Age": [20, 21, 20, 22, 21],
    "Marks": [85, 90, 78, 92, 88],
    "Department": ["Computer", "IT", "Computer", "ECE", "IT"]
}


# Create DataFrame
df = pd.DataFrame(students)


# Display DataFrame
print("\nStudent DataFrame:")
print(df)


# Display column names
print("\nColumn Names:")
print(df.columns)


# Display DataFrame index
print("\nDataFrame Index:")
print(df.index)


# Add a new column
df["Result"] = ["Pass", "Pass", "Pass", "Pass", "Pass"]


# Display updated DataFrame
print("\nUpdated DataFrame:")
print(df)