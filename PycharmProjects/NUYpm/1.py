import numpy as np

# Ocb - (Axes) Pozmirnost - (Dimension) Pang - (Rank)

#1 Odnomirniy masiv (Vector/Rank1)

arr_1d = np.array([1,2,3,4,5])
# print(arr_1d)
# print(f" 1D Array: ndim = {arr_1d.ndim} , shape = {arr_1d.shape}")

#2 Mirniy masiv (Matrix/Rank2)
matrix_2d = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
    ])
#
#
# print(matrix_2d)
# print(f" 1D Array: ndim = {matrix_2d.ndim} , shape = {matrix_2d.shape.shape}")

#3 Mirniy masiv (Rank3)
array_3d = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]],
    [[9,10],[11,12]]
])
#4) 4 Mirniy Masiv (Rank 4)