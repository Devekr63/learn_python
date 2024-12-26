"""
User input
"""
from datetime import date

first_name = input("Enter your first name: ").strip()

year_of_birth = int(input("Enter your year of birth: "))
month_of_birth = int(input("Enter your month of birth: "))
day_of_birth = int(input("Enter your day of birth: "))

# code to print age of the user

dob = date(year_of_birth, month_of_birth, day_of_birth)
days_in_year = 365.2425
age = int((date.today() - dob).days / days_in_year)

next_year_birth_date = date(date.today().year+1, month_of_birth, day_of_birth)
days_remain_in_birthday = int((next_year_birth_date - date.today()).days)

print(f"Hi, {first_name} your age is: {age}. "
      f"You have {days_remain_in_birthday} days for next birthday")