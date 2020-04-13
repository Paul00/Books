import numpy as np
arr = np.loadtxt('temp.csv',skiprows=1,usecols=(2,3),delimiter=',')
print(arr)
np.savetxt('temp.csv', arr, delimiter=',')
