import h5py
hdf5file = h5py.File('pytable_demo.hdf5')
arr=hdf5file['/global_power']
print(arr)
for i in range(len(arr)):
  print(arr[i])
hdf5file.close()
