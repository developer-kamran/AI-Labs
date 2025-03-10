# (i) Write a Python program to swap 4 variables values 
a, b, c, d = 2, 56, 78, 9

print("before swapping:")
print(f"a={a}, b={b}, c={c}, d={d}")
# before swapping:
# a=2, b=56, c=78, d=9

# swapping
a, b, c, d = d, c, b, a

# values after swapping
print("after swapping:")
print(f"a={a}, b={b}, c={c}, d={d}")
# after swapping:
# a=9, b=78, c=56, d=2


# (ii) Write a Python program to convert temperatures to and from celsius,

celsius = float(input("Enter temp in Celsius: "))

# conversion
fahrenheit = (celsius * 9 / 5) + 32

print(f"Temperature in Fahrenheit is: {fahrenheit}")
# Enter temp in Celsius: 60
# Temperature in Fahrenheit is: 140.0