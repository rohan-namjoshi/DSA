arr = [1,2,3,2,1,2,4,3,4,5,9,6,7,5,4,2,1]
f = {}
d = 0

for i in arr:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
for j in f.values():
    if j>1:
        d+=1
print(f"number of duplicates in {arr} = {d}" )
    