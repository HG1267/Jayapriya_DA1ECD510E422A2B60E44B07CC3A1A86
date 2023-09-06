#1.1 Implementation a recursion function to calculate the factorial of a given number.
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)


# Input a number to calculate its factorial
num = int(input("Enter a number: "))
if num < 0:
  print("Factorial is not defined for negative numbers.")
else:
  result = factorial(num)
  print(f"The factorial of {num} is {result}")
