# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 10:56:40 2020

@author: REGGIE
"""
生成一组数列，但可以重新切割成矩阵，reshape(),中间必须用括号括起来。
a = np.arange(1,26).reshape((5,5))


Out[25]: 
array([[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]])
    
    
前面是行，后面是列
a = np.ones((3,4))

a
Out[10]: 
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.]])
    
    
    
    
a = np.ones((3,4))

a
Out[10]: 
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.]])
    
    
 a = np.array([[1,2,3],
            [4,5,6]])    
   
线性数列的生成    
a = np.linspace(1,10,6).reshape((2,3))
Out[34]: 
array([[ 1. ,  2.8,  4.6],
       [ 6.4,  8.2, 10. ]])
    
python中的次方是用两个*号来表示   
c = b**2
Out[40]: array([0, 1, 4, 9], dtype=int32)


print(b<3)

[ True  True  True False]


a = np.random.random((2,4))

array([[0.34685854, 0.93915855, 0.2833196 , 0.86072681],
       [0.68887236, 0.44710422, 0.87846504, 0.99452588]])
    
1代表行间，0代表列间
print(np.sum(a,axis = 1))    
[2.4300635 3.0089675]

print(np.sum(a,axis = 0))
[1.0357309  1.38626277 1.16178463 1.85525269]


A = np.arange(15).reshape((3,5))

array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])

最小值的索引    
print(np.argmin(A))
0

数列的转向
print(A.T)
[[ 0  5 10]
 [ 1  6 11]
 [ 2  7 12]
 [ 3  8 13]
 [ 4  9 14]]

a = np.arange(15).reshape((3,5))

array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])


单个值代表一行
a[2]
Out[63]: array([10, 11, 12, 13, 14])

第一个值代表行，第二个值代表列
a[1][3]
Out[65]: 8
a[1,3]
Out[66]: 8

冒号代表第二行中的所有数
a[2,:]
Out[67]: array([10, 11, 12, 13, 14])

冒号代表第二列中的所有数
a[:,2]
Out[68]: array([ 2,  7, 12])

第一行的，第0到1的值。
a[1,0:2]
Out[69]: array([5, 6])

第一个冒号代表所有行，第二个冒号代表所有列，第三个冒号代表每隔一个数，取一个值
a[:,::2]
Out[75]: 
array([[ 0,  2,  4],
       [ 5,  7,  9],
       [10, 12, 14]])
 
第一个冒号代表所有行，1::2，代表从第一列到最后列开始取值，中间有一个间隔。    
a[:,1::2]
Out[76]: 
array([[ 1,  3],
       [ 6,  8],
       [11, 13]])
    
1:,代表从第一行开始取值，3:，从第三列开始取值。    
a[1:,3:]
Out[79]: 
array([[ 8,  9],
       [13, 14]])    
    
    

a = np.arange(25).reshape((5,5))

array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19],
       [20, 21, 22, 23, 24]])

a[2:,:]
Out[8]: 
array([[10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19],
       [20, 21, 22, 23, 24]])

所有行中间隔一行取    
a[::2]
Out[9]: 
array([[ 0,  1,  2,  3,  4],
       [10, 11, 12, 13, 14],
       [20, 21, 22, 23, 24]])

所有行中间隔一行取，列从第一列到最后列，中间隔一行取值。    
a[::2,1::2]
Out[10]: 
array([[ 1,  3],
       [11, 13],
       [21, 23]])    