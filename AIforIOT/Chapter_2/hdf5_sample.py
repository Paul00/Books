import numpy as np
arr = np.loadtxt('temp.csv', skiprows=1, usecols=(2,3), delimiter=',')

import tables
h5filename = 'pytable_demo.hdf5'
with tables.open_file(h5filename,mode='w') as h5file:
  root = h5file.root
  h5file.create_array(root, 'global_power', arr)
  h5file.close()

with tables.open_file(h5filename, mode='r') as h5file:
  root = h5file.root
  for node in h5file.root:
    ds = node.read()
    print(type(ds), ds.shape)
    print(ds)
