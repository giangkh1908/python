import numpy as np

# create 2-dimensional array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr[0, 0])
print(arr[1, 1])

# slicing
# print(arr[0, :2])
# print(arr[0:, 0:])

print(arr[:, 0])
print(arr[1, :])

print(arr[:, 1:2])