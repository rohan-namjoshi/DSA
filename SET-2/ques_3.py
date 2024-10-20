nums = [3, 2, 1, 5, 6, 4]
k = 2

heap = nums[:k]

for i in range((k // 2) - 1, -1, -1):
    root = i
    while True:
        left = 2 * root + 1
        right = 2 * root + 2
        smallest = root

        if left < k and heap[left] < heap[smallest]:
            smallest = left
        if right < k and heap[right] < heap[smallest]:
            smallest = right
        if smallest != root:
            heap[root], heap[smallest] = heap[smallest], heap[root]
            root = smallest
        else:
            break

for i in range(k, len(nums)):
    if nums[i] > heap[0]:
        heap[0] = nums[i]
        root = 0
        while True:
            left = 2 * root + 1
            right = 2 * root + 2
            smallest = root

            if left < k and heap[left] < heap[smallest]:
                smallest = left
            if right < k and heap[right] < heap[smallest]:
                smallest = right
            if smallest != root:
                heap[root], heap[smallest] = heap[smallest], heap[root]
                root = smallest
            else:
                break

print(f"The {k}th largest element is: {heap[0]}")
