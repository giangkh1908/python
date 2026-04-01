"""Numpy operations"""

import numpy as np

# arr_1 = np.array([1, 2, 3])
# arr_2 = np.array([4, 5, 6])

# # addition
# result = arr_1 + arr_2
# print(result)  # Output: [5 7 9]

# # subtraction
# result = arr_1 - arr_2
# print(result)  # Output: [-3 -3 -3]

# # multiplication
# result = arr_1 * arr_2
# print(result)  # Output: [4 10 18]

# # division
# result = arr_1 / arr_2
# print(result)  # Output: [0.25 0.4 0.5]


# print("Tong cua cac phan tu trong arr_1: ", np.sum(arr_1))  # Output: 6

# print("Tong cua cac phan tu trong arr_1: ", arr_1.sum())  # Output: 6


# array 2 chieu
arr_1 = np.array([[1, 2, 3], [4, 5, 6]])
arr_2 = np.array([[7, 8, 9], [10, 11, 12]])

# print("tong cua tung row: ", np.sum(arr_1, axis=1))  # Output: [5 7 9]
# print("tong cua tung column: ", np.sum(arr_1, axis=0))  # Output: [5 7 9]

# # when hold dimension like array ban đầu
# print("tong cua tung row: ", np.sum(arr_1, axis=1, keepdims=True))  # Output: [[5] [7] [9]]
# print("tong cua tung column: ", np.sum(arr_1, axis=0, keepdims=True))  # Output: [[5 7 9]]

print("Max: ", arr_1.max())  # Output: 6
print("Min: ", arr_1.min())  # Output: 1
print("Mean: ", arr_1.mean())  # Output: 3.5




