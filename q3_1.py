def merge_sorted_arrays(arr1, arr2):
  merged_arr = []
  i = 0
  j = 0

  while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:
      merged_arr.append(arr1[i])
      i += 1
    else:
      merged_arr.append(arr2[j])
      j += 1

  merged_arr += arr1[i:]
  merged_arr += arr2[j:]

  return merged_arr


arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
merged_arr = merge_sorted_arrays(arr1, arr2)
print("Merged array:", merged_arr)