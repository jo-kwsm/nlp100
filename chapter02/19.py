from operator import itemgetter
import numpy as np
f=open("chapter02/popular-names.txt")
flist=f.readlines()
l=list()
cnt=dict()
for i in flist:
  a=i.split()[0]
  if a in cnt:
    cnt[a]+=1
  else:
    cnt[a]=1
for i in flist:
  a,b,c,d=i.split()
  l.append([cnt[a],a,b,c,d])
l.sort(reverse=True)
l=np.array(l)[:,1:]
print(l)