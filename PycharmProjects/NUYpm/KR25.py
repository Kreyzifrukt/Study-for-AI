import numpy as np

# 1
arr1 = np.array([1, 2, 3, 4, 5, 6])
print(arr1)                 # вміст
print(arr1.dtype)           # тип даних

arr1_float = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
print(arr1_float.dtype)     # float64
# 2
arr2 = np.arange(10, 100, 10).reshape(3, 3)
print(arr2)
print(arr2.shape)
print(arr2.size)
# 3
arr3 = np.array([
    [[1, 2],
     [3, 4]],

    [[5, 6],
     [7, 8]]
])

print(arr3.ndim)
print(arr3)
# 4
my_list = [10, 20, 30, 40]
arr4 = np.array(my_list, dtype=np.int8)
print(arr4)
print(arr4.dtype)   # int8
# 5
good_array = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(good_array)
print(good_array.shape)   # (2, 3)