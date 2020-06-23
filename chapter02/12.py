import numpy as np
f=open("chapter02/popular-names.txt")
flist=f.readlines()
flist=np.array([file.split("\t") for file in flist])
col1="\n".join(flist[:,0])
col2="\n".join(flist[:,1])

with open("chapter02/col1.txt",'w') as f:
  f.write(col1)
with open("chapter02/col2.txt",'w') as f:
  f.write(col2)
