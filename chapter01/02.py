s1="パトカー"
s2="タクシー"
s=""
for i in range(len(s1+s2)):
  if i%2:
    s=s+s2[i//2]
  else:
    s=s+s1[i//2]

print(s)