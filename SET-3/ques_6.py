def is_palindrome(str):
    return str == str[::-1]


def is_cyclic_palindrome(str):
    n = len(str)
    if is_palindrome(str):
        return 1

    for i in range (1,n):
        str = str[1:] + str[0]
        if is_palindrome(str):
            return 1
    return -1

str = input("enter a string: ")
print(is_cyclic_palindrome(str))
