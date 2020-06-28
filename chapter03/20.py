import json
f=open("chapter03/jawiki-country.json")
flist=f.readlines()
for i in flist:
  page=json.loads(i)
  if page["title"]=="イギリス":
    print(page["text"])