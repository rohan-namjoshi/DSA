def count_negative_integers(arr):
  count = 0
  for num in arr:
    if num < 0:
      count += 1
  return count

arr = [-1, 2, -3, 4, -5]
result = count_negative_integers(arr)
print("Number of negative integers:", result)