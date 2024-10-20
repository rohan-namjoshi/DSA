arr = [-7, 1, 5, 2, -4, 3, 0]

total_sum = sum(arr)
left_sum = 0

for i in range(len(arr)):
    
    right_sum = total_sum - left_sum - arr[i]
    
   
    if left_sum == right_sum:
        print(f"Equilibrium index: {i + 1}")  
        break
    
    left_sum += arr[i]
else:
    print("No equilibrium index exists")
