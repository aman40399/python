import numpy as np

# Creating a 1D array from a list
arr1d = np.array([1, 2, 3, 4, 5])

# Creating a 2D array from a list of lists
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Creating a 2D array of zeros with dimensions 4x5
arr_zeros = np.zeros((4, 5),dtype=int)

print("1D array:")
print(arr1d)

print("\n2D array:")
print(arr2d)
 
print("2D-0 array:")
print(arr_zeros)
#functions in numpy libray


# Creating a 1D array of random numbers
arr_random = np.random.rand(5)

print("\n1D array of random numbers:")
print(arr_random)

# Creating a DataFrame from a 2D array
import pandas as pd

df = pd.DataFrame(arr2d)

print("\nDataFrame of the 2D array:")
print(df)


