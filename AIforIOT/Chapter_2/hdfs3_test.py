from hdfs3 import HDFileSystem
hdfs = HDFileSystem(host = 'localhost', port=8020)

print(hdfs.ls('/tmp'))

with hdfs.open('/tmp/file1.txt','wb') as f:
  f.write(b'You are Awesome!')

with hdfs.open('/tmp/file1.txt') as f:
  print(f.read())

