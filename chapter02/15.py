f=open("chapter02/popular-names.txt")
flist=f.readlines()
n=int(input())

for i in range(min(n,len(flist))):
  print(flist[-(i+1)].replace("\n",""))