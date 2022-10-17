# 1
# Given are 2 similar dimensional numpy arrays, 
# how to get a numpy array output in which every element is an element-wise sum of the 2 numpy arrays? 
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
arr2 = np.array([1, 2, 3, 4, 5])
arrSum=[]
for x in range(0,len(arr)):
    arrSum.append(arr[x]+arr2[x])
    x+=1
print(arrSum)

# 2
# Convert a 1-D array to a 3-D array

from array import array
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr_3d = np.reshape(arr, (2, 2, 3))
print('3D Numpy array:')
print(arr_3d)

# 3
# Create an identity matrix of dimension 4-by-4

from array import array
import numpy as np
a = np.identity(4)
print(a)
# 4
# Convert all the elements of a numpy array from float to integer datatype

from array import array
import numpy as np
og_array = np.array([[11.21, 19.21], [46.21, 18.21], [29.21, 21.21]])
print(og_array)
int_array = og_array.astype(int)
print(int_array)

# 5
# Convert a binary numpy array (containing only 0s and 1s) to a boolean numpy array

from array import array
import numpy as np
og_array = np.array([[0,0,1,0,0],[1,0,0,1,0], [1,0,1,0,0]]) 
print(og_array)
bool_array = og_array.astype(bool)
print(bool_array)
# 6
# Stack 2 numpy arrays vertically i.e., 2 arrays having the same last dimension (number of columns in 2D arrays)
import numpy as np

arr1 = [1,2,3]
arr2 = [4,5,6]
print(arr1)
print(arr2)
a = np.column_stack([arr1, arr2])
print(a)

# 7
# Generate a sequence of numbers in the form of a numpy array from 0 to 100 with gaps of 2 numbers, for example: 0, 2, 4 ....
import numpy as np

arr1 = np.arange(0,100,2)
print(arr1)
# 8
# Output a sequence of equally gapped 5 numbers in the range 0 to 100 (both inclusive)
import numpy as np

arr1 = np.linspace(0,100,5)
print(arr1)

# 9
# Output a 5-by-5 array of random integers between 0 (inclusive) and 10 (exclusive)

import numpy as np
np.random.seed(345) 
a = np.random.randint(0, 10, size = (5,5))
print(a)

# 10
# Given 2 numpy arrays as matrices, output the result of multiplying the 2 matrices (as a numpy array)

import numpy as np
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

b = np.array([[2,3,4],
              [5,6,7],
              [8,9,10]])
res = np.matmul(a,b)
print(res)

# 11
# Calculate the sine of an array of angles (in radians) using NumPy

import numpy as np
angles = np.array([3.14, 3.14/2, 6.28])
sine_of_angles = np.sin(angles)
print('Result = ', sine_of_angles)

# 12
#Calculate the cosine similarity of 2 vectors (as numpy arrays)


import numpy as np
angles = np.array([3.14, 3.14/2, 6.28])
cosine_of_angles = np.cos(angles)
print('Res = ', cosine_of_angles)

# 13
# Calculate the cosine similarity of 2 vectors (as numpy arrays)

import numpy as np
a = np.array([[1,2,3],
              [4,5,6]])
b = 2*a 
print(b)