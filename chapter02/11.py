f=open("chapter02/popular-names.txt")
flist=f.readlines()
for line in flist:
  line=line.replace("\t"," ")
  print(line)