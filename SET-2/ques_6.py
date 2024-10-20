A = [1, 2, 4, 5, 7, 11]
N = 6
X = 9
left = 0
right = N - 1
found = False

while left < right:
    current_sum = A[left] + A[right]
    if current_sum == X:
        found = True
        break
    elif current_sum < X:
        left += 1
    else:
        right -= 1

if found:
    print("Yes")
else:
    print("No")
