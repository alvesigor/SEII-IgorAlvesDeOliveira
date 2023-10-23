import numpy as np

data = np.loadtxt('ARQUIVO.csv',delimiter = ",",dtype= np.float32)
print(data)

data = np.genfromtxt('ARQUIVO.csv',delimiter=',',dtype=np.float32)
print(data.shape)