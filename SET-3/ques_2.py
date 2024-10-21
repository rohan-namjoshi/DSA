l=[1,4,6]
var=0
for i in range(len(l)):
    for j in range(i,len(l)):
        var|=l[j]
print(var)   
  
