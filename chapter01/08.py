def cipher(c):
  if ('a'<=c)&(c<='z'):
    c=str(219-c.stoi())
  return c

s='abcABC'
s=[cipher(i) for i in s]
print(s)