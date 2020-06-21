import random
s="I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
def typoglycemia(c):
  slist=c.split()
  for i in range(len(slist)):
    if len(slist[i])<=4:
      continue
    rs=list(slist[i][1:-1])
    random.shuffle(rs)
    slist[i]=slist[i][0]+"".join(rs)+slist[i][-1]
  return " ".join(slist)

print(typoglycemia(s))