s="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
slist=s.split()
slist=[i.split(",")[0] for i in slist]
slist=[i.split(".")[0] for i in slist]
nlist=[len(slist[idx]) for idx in range(len(slist))]
print(nlist)