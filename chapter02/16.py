f=open("chapter02/popular-names.txt")
flist=f.readlines()
n=int(input())
flist=[flist[i::n] for i in range(n)]
print(flist)