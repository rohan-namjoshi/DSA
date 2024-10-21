def square_free(x):
  if x<=1:
    return 0

  for i in range(2,int(x**0.5)+1):
    if x % (i*i) == 0:
      return 0
  return 1

def count(x):
    counter = 0
    for i in range(1,x+1):
        if x % i == 0 and square_free(i):
            counter += 1
      
    return counter

n = int(input("Enter a number: "))

z = count(n)

print(f"number of square free factors: {z}")
