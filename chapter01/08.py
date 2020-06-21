def cipher(c):
  res=""
  for i in c:
    if 'a'<=i<='z':
      res=res+chr(219-ord(i))
    else:
      res=res+i
  return res

s='abcABC'
print(cipher(s))