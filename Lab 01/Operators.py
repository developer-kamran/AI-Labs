# 1. Identity Operators in Python:
x = 6
if (type(x) is int):
    print ("true")
else:
    print ("false")

# Output: True

x = 7.2
if (type(x) is not int):
    print ("true")
else:
    print ("false")

# Output: True


# 3. Membership Operator:
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
for item in list1:
    if item in list2:
        print("overlapping")
else:
    print("not overlapping")

# Output: not overlapping


# 4. Floor Division and Exponentiation:
a = 5
a //= 3  # floor division
a **= 5  # exponentiation 
print("floor divide=", a)
print("exponent=", a)

# Output: floor divide= 1
# Output: exponent= 1


# 5. Bitwise Operators:
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b  # Bitwise AND (12 = 0000 1100)
print("Line 1", c)

c = a | b  # Bitwise OR (61 = 0011 1101)
print("Line 2", c)

c = a ^ b  # Bitwise XOR (49 = 0011 0001)
print("Line 3", c)

c = ~a     # Bitwise NOT (-61 = 1100 0011)
print("Line 4", c)

c = a << 2  # Bitwise Left Shift (240 = 1111 0000)
print("Line 5", c)

c = a >> 2  # Bitwise Right Shift (15 = 0000 1111)
print("Line 6", c)

# Output:
# Line 1 12
# Line 2 61
# Line 3 49
# Line 4 -61
# Line 5 240
# Line 6 15