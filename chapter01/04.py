s="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
slist=s.split()
one={1,5,6,7,8,9,15,16,19}
ans={}
for i in range(len(slist)):
  if one&{i+1}:
    ans[i+1]=slist[i][0]
  else:
    ans[i+1]=slist[i][0:2]
print(ans)