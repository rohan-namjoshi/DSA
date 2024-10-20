nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_current = nums[0]
max_global = nums[0]

for i in range(1, len(nums)):
    num = nums[i]
    max_current = max(num, max_current + num)
    if max_current > max_global:
        max_global = max_current

print(f"The largest sum of a subarray is: {max_global}")
