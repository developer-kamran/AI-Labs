# I. a Python program to square and cube every number in a given list of integers using Lambda. 

numbers = [7, 5, 4, 3, 6]

square = list(map(lambda x: x ** 2, numbers))
cube = list(map(lambda x: x ** 3, numbers))

print("Squared:", square)
print("Cubed:", cube)


# II. a Python program to find if a given string starts with a given character using Lambda. 

starts_with = lambda string, char: string.startswith(char)

string = "University Of Karachi"
char = "U"

print(f"Does '{string}' start with '{char}'?", starts_with(string, char))


# III. a Python program to extract year, month, date and time using Lambda.

from datetime import datetime

now = datetime.now()

extract = lambda dt: (dt.year, dt.month, dt.day, dt.time())

year, month, day, time = extract(now)

print("Year:", year)
print("Month:", month)
print("Day:", day)
print("Time:", time)
