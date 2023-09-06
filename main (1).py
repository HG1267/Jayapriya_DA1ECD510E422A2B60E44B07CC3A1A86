#1.2 write a program that determines whether a year ended by the user is a leap year or not using if elif- else statements.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print(year, "is a leap year.")
else:
  print(year, "is not a leap year.")
