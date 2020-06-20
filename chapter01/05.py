def n_gram(s,n):
  res=[s[i:i+n] for i in range(len(s)-n+1)]
  return res

s="I am an NLPer"
slist=s.split()
sgram=n_gram(s,2)
slistgram=[n_gram(i,2) for i in slist]
print(sgram)
print(slistgram)