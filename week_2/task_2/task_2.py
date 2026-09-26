import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Original 1D array:")
print(numbers)

#Access specific elements using indexing
print("\n Indexing:")
print("Element at index 0:", numbers[0])
print("Element at index 3:", numbers[3])
print("Last element:", numbers[-1])

#Extract a portion of the array using slicing
print("\nSlicing:")
print("Elements from index 2 to 5:", numbers[2:6])
print("First five elements:", numbers[:5])
print("Last three elements:", numbers[-3:])
print("Every second element:", numbers[::2])
print("Reversed array:", numbers[::-1])

#Create a two-dimensional array
two_d_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nTwo-dimensional array:")
print(two_d_array)

#Access specific rows and columns
print("\nAccessing rows and columns:")
print("First row:", two_d_array[0, :])
print("Second column:", two_d_array[:, 1])
print("Element at row 2, column 3:", two_d_array[1, 2])

#Reshape an array into different dimensions
reshape_numbers = np.arange(1, 13)

print("\nOriginal 1D array for reshaping:")
print(reshape_numbers)

#Reshape into a 3x4 array
reshaped_3x4 = reshape_numbers.reshape(3, 4)
print("\nReshaped into 3x4 array:")
print(reshaped_3x4)

#Reshape into a 4x3 array
reshaped_4x3 = reshape_numbers.reshape(4, 3)  
print("\nReshaped into 4x3 array:")
print(reshaped_4x3)

#Reshape into a 2x2x3 array
reshaped_2x2x3 = reshape_numbers.reshape(2, 2, 3)
print("\nReshaped into 3 Dimensions (2x2x3) array:")
print(reshaped_2x2x3)
