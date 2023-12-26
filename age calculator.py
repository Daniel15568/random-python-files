error = True
while error:
  error = False
  try:
    name = input("Welcome to Age Calculator! \nWhat\'s your name: ")
    day_of = int(input("Enter birth date: "))
    month_of_birth = int(input("Enter birth month: "))
    year = int(input("Enter birth year: "))
    
  except (ValueError, SyntaxError):
    print("Invalid input, Try Again")
    error = True

def find_day(day):
  if month_of_birth == 2:
        day = 28 - day_of
  elif year%4 == 0 or year % 100 == 0 or year % 400 == 0 and month_of_birth == 2:
        day = 29 - day_of
  elif month_of_birth in [1, 3, 5, 7, 8, 10, 12]:
        day = 31 - day_of
  elif month_of_birth in [4, 6, 9, 11]:
        day = 30 - day_of
  return day

day = 0
if 0 < day_of < 32:
  day = find_day(day_of)
else:
  print("invalid date")

month = 0
if 0 < month_of_birth < 13:
  month = 12 - month_of_birth
else:
  print("invalid month")

years = 0
if 1900 < year < 2023:
  years = 2023 - year
else:
  print("invalid year")

print(f"Hi {name}!\nYou are {years} years, {month} months and {day} days.")