nums = [5, 6, -5, 5, 3, 5, 3, -2, 0]
target = 8

sum_map = {}  
max_length = 0
cumulative_sum = 0
start_index = 0
end_index = -1

for i in range(len(nums)):
    cumulative_sum += nums[i]

    if cumulative_sum == target:
        max_length = i + 1
        end_index = i

    if (cumulative_sum - target) in sum_map:
        if i - sum_map[cumulative_sum - target] > max_length:
            max_length = i - sum_map[cumulative_sum - target]
            start_index = sum_map[cumulative_sum - target] + 1
            end_index = i

    if cumulative_sum not in sum_map:
        sum_map[cumulative_sum] = i

if end_index == -1:
    print("No subarray with given sum")
else:
    print(f"Maximum length subarray with sum {target}: {nums[start_index:end_index + 1]}")
