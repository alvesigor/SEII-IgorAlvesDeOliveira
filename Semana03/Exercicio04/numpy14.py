import numpy as np

a = np.array([[1,2],[3,4]])

autoval, autovetor = np.linalg.eig(a)

print(autoval, '\n')
print(autovetor,'\n')


b = autovetor[:,0] * autoval[0]
print(b)

c = a @ autovetor[:,0]
print(c)

print(b==c)
print (np.allclose(b,c))

#Resolvendo o sistema linear

A = np.array([[1,1],[1.5,4.0]])
B = np.array([2200,5050])

X = np.linalg.inv(A).dot(B)
print (X)

X = np.linalg.solve(A,B)
print(X)