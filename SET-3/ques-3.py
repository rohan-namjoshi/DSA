def max_sub(arr, n, K):

    useful_elements = []
    result = []

    for i in range(K):
        while useful_elements and arr[useful_elements[-1]] <= arr[i]:
            useful_elements.pop()
        useful_elements.append(i)

    for i in range(K, n):
        result.append(arr[useful_elements[0]])

        while useful_elements and useful_elements[0] <= i - K:
            useful_elements.pop(0)

        while useful_elements and arr[useful_elements[-1]] <= arr[i]:
            useful_elements.pop()

        useful_elements.append(i)

    result.append(arr[useful_elements[0]])

    return result

arr1 = [1, 2, 3, 1, 4, 5]
K1 = 3
print(max_sub(arr1, len(arr1), K1))

arr2 = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
K2 = 4
print(max_sub(arr2, len(arr2), K2))

arr3 = [20, 10, 30]
K3 = 1
print(max_sub(arr3, len(arr3), K3))
