f=open("chapter02/popular-names.txt")
flist=f.readlines()
s=set()
for i in flist:
  s.add(i.split()[0])

print(len(s))