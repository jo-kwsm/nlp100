col1=open("chapter02/col1.txt")
col2=open("chapter02/col2.txt")

col1=col1.readlines()
col2=col2.readlines()

s=""
for a,b in zip(col1,col2):
  s=s+a.replace("\n","")+'\t'+b

with open("chapter02/col12.txt",'w') as f:
  f.write(s)