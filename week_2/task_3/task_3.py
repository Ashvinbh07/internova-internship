import numpy as np

#Mathematical operations:

week1 = np.array([100, 200, 300, 400, 500])
week2 = np.array([50, 100, 150, 200, 250])

print("Week 1 sales data:")
print(week1)
print("\nWeek 2 sales data:")
print(week2)

addition = np.add(week1, week2)
print("\nAddition:")
print(addition)

subtraction = np.subtract(week1, week2)
print("\nSubtraction:")
print(subtraction)

multiplication = np.multiply(week1, week2)
print("\nMultiplication:")  
print(multiplication)

division = np.divide(week1, week2)
print("\nDivision:")
print(division)

#Statistical Operations:

sales = np.array([120, 250, 180, 300, 150, 400, 220, 350, 280, 200])

print("\nSales data:")
print(sales)

print("\nMean:", np.mean(sales))
print("Median:", np.median(sales))
print("Minimum:", np.min(sales))
print("Maximum:", np.max(sales))
print("Standard Deviation:", np.std(sales))
print("Sum:", np.sum(sales))