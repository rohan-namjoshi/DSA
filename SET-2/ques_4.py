s = "A man, a plan, a canal: Panama"

lowercase_s = ""
for char in s:
    if 'A' <= char <= 'Z':
        lowercase_s += 'abcdefghijklmnopqrstuvwxyz'['ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(char)]
    else:
        lowercase_s += char

cleaned = ""
for char in lowercase_s:
    if ('a' <= char <= 'z') or ('0' <= char <= '9'):
        cleaned += char

is_palindrome = True
left = 0
right = len(cleaned) - 1

while left < right:
    if cleaned[left] != cleaned[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

print(is_palindrome)  
