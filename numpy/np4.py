import numpy as np

# create array full value 0
# zeros_arr = np.zeros((3, 3))
# print(zeros_arr)  # Output: [0. 0. 0. 0.]

# create array full value 1
# ones_arr = np.ones((3, ))
# print(ones_arr)  # Output: [[1. 1. 1.] [1. 1. 1.] [1. 1. 1.]]

# create arrray have value 1 to 9
# arange_arr = np.arange(10)  # Output: [0 1 2 3 4 5 6 7 8 9]
# print(arange_arr)  # Output: [1 2 3 4 5 6 7 8 9]

# # create array have value 1 to 9 with step 2
# arange_step_arr = np.arange(0, 11, 2)
# print(arange_step_arr)  # Output: [[0 2 4 6 8 10]]

# linespace() - create array with specified number of elements between a range
new_arr = np.linspace(0, 10, num = 5)
print(new_arr)  # Output: [ 0.  2.5 5.  7.5 10. ]


x = np.ones((2,)) # auto float
y = np.ones((2,), dtype=np.int64) # int
print(x.dtype)
print(x)
print(y.dtype)
print(y)



