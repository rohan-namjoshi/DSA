def max_of_subarrays(arr, n, K):
    # List to store indices of useful elements in the window
    useful_elements = []
    result = []

    # Process the first K elements
    for i in range(K):
        # Remove elements that are smaller than the current element
        while useful_elements and arr[useful_elements[-1]] <= arr[i]:
            useful_elements.pop()
        # Add the current element's index
        useful_elements.append(i)

    # Process the rest of the elements
    for i in range(K, n):
        # The element at the front of the list is the largest of the previous window
        result.append(arr[useful_elements[0]])

        # Remove elements not in the current window
        while useful_elements and useful_elements[0] <= i - K:
            useful_elements.pop(0)

        # Remove elements smaller than the current element
        while useful_elements and arr[useful_elements[-1]] <= arr[i]:
            useful_elements.pop()

        # Add the current element's index
        useful_elements.append(i)

    # Add the maximum of the last window
    result.append(arr[useful_elements[0]])

    return result

# Test cases
arr1 = [1, 2, 3, 1, 4, 5]
K1 = 3
print(max_of_subarrays(arr1, len(arr1), K1))  # Output: [3, 3, 4, 5]

arr2 = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
K2 = 4
print(max_of_subarrays(arr2, len(arr2), K2))  # Output: [10, 10, 10, 15, 15, 90, 90]

arr3 = [20, 10, 30]
K3 = 1
print(max_of_subarrays(arr3, len(arr3), K3))  # Output: [20, 10,
