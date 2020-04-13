import pandas as pd
import numpy as np

arr = np.loadtxt('temp.csv', skiprows=1, usecols=(2,3), delimiter=',')
print(arr)
store=pd.HDFStore('hdfstore_demo.hdf5')
print(store)
store['global_power']=pd.DataFrame(arr)
store.close()

import pandas as pd
store=pd.HDFStore('hdfstore_demo.hdf5')
print(store)
print(store['global_power'])
store.close()
