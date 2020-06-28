from operator import itemgetter

f=open("chapter02/popular-names.txt")
flist=f.readlines()
l=list()
for i in flist:
  a,b,c,d=i.split()
  l.append([a,b,int(c),d])
l.sort(key=itemgetter(2))
print(l)