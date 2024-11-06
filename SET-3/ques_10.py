def min_p(arr, n, k):
    arr.sort()
    
    product = 1
    
    for i in range (k):
        product = product * arr[i]
        
    return product
    
arr = [1,2,3,4,5]
n = len(arr)
k = int(input("enter k: "))

print("minimum product for k elements: ", min_p(arr,n,k))
