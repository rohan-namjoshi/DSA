arr = [1,2,4,33,3,3,2,2,1,0,1,9,8,7,6,5]
f = {}

for i in arr:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
print(f"frequency of each number = {f}")
    
