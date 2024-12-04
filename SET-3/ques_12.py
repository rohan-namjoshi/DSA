def is_happy_number(n):
    def sum_of_squares(num):
        return sum(int(digit) ** 2 for digit in str(num))

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum_of_squares(n)

    return n == 1


number = 19
if is_happy_number(number):
    print(f"{number} is a Happy Number!")
else:
    print(f"{number} is not a Happy Number.")

