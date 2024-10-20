arr = [7, 2, 6, 3]
n = len(arr)

temp_arr = [0] * n
inv_count = 0

left = 0
right = n - 1
stack = [(left, right)]

while stack:
    left, right = stack.pop()
    if left < right:
        mid = (left + right) // 2
        
        stack.append((left, mid))
        stack.append((mid + 1, right))
        
        i = left
        j = mid + 1
        k = left
        
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                temp_arr[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1
        
        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1
        
        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1
        
        for i in range(left, right + 1):
            arr[i] = temp_arr[i]

print(f"Number of inversions: {inv_count}")
