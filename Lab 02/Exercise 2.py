## EXERCISE 2:

# (i) What Would Python Print?
n = 3
while n >= 0:
    n -= 1
    print(n)

# Output:
# 2
# 1
# 0
# -1

# (ii) What Would Python Print? (Infinite Loop Example)
n = 4
while n > 0:
    n += 1  # This causes an infinite loop as n keeps increasing
    print(n)


# (I) Try the scenrio below:

# Make a program that lists the countries in the set

clist = ['Canada', 'USA', 'Mexico', 'Australia']
for country in clist:
    print(country)

# 1. Create a loop that counts from 0 to 100
for i in range(101):
    print(i)

# 2. Make a multiplication table using a loop
num = int(input("Enter a number for multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 3. Output the numbers 1 to 10 backwards using a loop
for i in range(10, 0, -1):
    print(i)

# 4. Create a loop that counts all even numbers to 10
for i in range(0, 11, 2):
    print(i)

# 5. Create a loop that sums the numbers from 100 to 200
total = sum(range(100, 201))
print("Sum of numbers from 100 to 200:", total)


# (II) Try the exercise below:

# (1) Make a program that lists the countries in the set below using a while loop.

clist = ["Canada", "USA", "Mexico"]
i = 0
while i < len(clist):
    print(clist[i])
    i += 1

# (2) Difference between while loop and for loop
# - A while loop runs as long as a condition is true, useful when the number of iterations is unknown.
# - A for loop iterates over a sequence (e.g., list, range), useful when the number of iterations is known.

# (3) Can you sum numbers in a while loop?
sum_total = 0
n = 1
while n <= 10:
    sum_total += n
    n += 1
print("Sum of numbers from 1 to 10:", sum_total)

# (4) Can a for loop be used inside a while loop?
count = 0
while count < 2:
    for i in range(1, 4):
        print(f"Iteration {i} inside while loop cycle {count+1}")
    count += 1
