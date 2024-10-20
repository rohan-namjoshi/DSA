arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4

n = len(arr)
if k > n:
    print("Invalid")
else:
    max_sum = 0
    for i in range(k):
        max_sum += arr[i]
    

    window_sum = max_sum
    
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        if window_sum > max_sum:
            max_sum = window_sum
            
    print(max_sum)
