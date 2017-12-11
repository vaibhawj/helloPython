name = input("Enter name: ")

while(True):
    try:
        age = int(input("Enter age: "))
        break
    except ValueError:
        print("Invalid input")

number_of_years_to_100 = 100 - age

import datetime

now = datetime.datetime.now()

current_year = now.year

print("Hi {0}, you will become 100 years in {1}".format(name, current_year + number_of_years_to_100))
