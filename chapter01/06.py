def n_gram(s,n):
  res=[s[i:i+n] for i in range(len(s)-n+1)]
  return res

s1="paraparaparadise"
s2="paragraph"

s1list=set(n_gram(s1,2))
s2list=set(n_gram(s2,2))
wa=s1list|s2list
seki=s1list&s2list
sa=s1list^s2list
print(wa)
print(seki)
print(sa)
print("xに",end="")
if s1list&{"se"}:
  print("含まれる")
else:
  print("含まれない")

print("yに",end="")
if s2list&{"se"}:
  print("含まれる")
else:
  print("含まれない")