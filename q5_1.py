def is_palindrome(s):
    return s==s[::-1]
num = []

for i in range(5):
    n = int(input("enter a number: "))
    num.append(n)
if is_palindrome(num):
    print("is a palindrome input")
else:
    print("not a palindrome input")