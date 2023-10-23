import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8]])
print(a)

#index
b = a[0,1:4]
print(b)

#bool_index

bool_index = a > 2 
print(bool_index)

c = np.where(a>2,a,-1)
print(c)

d = np.array([10,19,26,20,30,40,50,93])

even = np.argwhere(a%2 == 0).flatten()

print(d[even])