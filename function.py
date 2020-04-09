import numpy as np

def forbeniusvNorm(np_arr):
    #表示A矩阵没饿元素的平方和的开方值，用来衡量矩阵的大小，或者比较矩阵之间的距离
    return np.sqrt(np.sum(np_arr**2))
