#Imports NumPy
import numpy as np

#Creates a NumPy array containing at least 10 numbers
numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

#Displays the array
print("Original array:")
print(numbers)

#Displays the array's shape, size, and data type
print("\nShape:", numbers.shape)
print("Size:", numbers.size)
print("Data Type:", numbers.dtype)

#Creates a one-dimensional and two-dimensional array
one_d_array = np.array([1, 2, 3, 4, 5])

print("\nOne-dimensional array:")
print(one_d_array)

two_d_array = np.array([[1, 2, 3], [4, 5, 6]])
print("\nTwo-dimensional array:")
print(two_d_array)