import numpy as np

arr_1d = np.array([1, 2, 3])
arr_2d = np.array([[1, 2], [3, 4]])

# ndim - số chiều của mảng
# print(arr_1d.ndim)  # Output: 1
# print(arr_2d.ndim)  # Output: 2

# shape - số lượng phần tử trong mỗi chiều của mảng - tuple
# print(arr_1d.shape)  # Output: (3,)
# print(arr_2d.shape)  # Output: (2, 2)

# # size - tổng số phần tử trong mảng
# print(arr_1d.size)  # Output: 3
# print(arr_2d.size)  # Output: 4

# dtype - kiểu dữ liệu của các phần tử trong mảng
print(arr_1d.dtype)  # Output: int64
print(arr_2d.dtype)  # Output: int64

# vi sao phai convert
new_arr_2d = arr_2d.astype(np.float64)
print(new_arr_2d.dtype)  # Output: float64