# (i) Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
sample_list = ['abc', 'xyz', 'aba', '1221']

count = 0

for s in sample_list:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1

print("Number of strings meeting the criteria:", count)
# Number of strings meeting the criteria: 2


# (ii) Write a list comprehension which, from a list, generates a lowercased version of each string that has length greater than five. 

list = ['HelloWorld', 'Python', 'AI', 'DeepLearning']

result = []
for s in sample_list:
    if len(s) > 5:
        result.append(s.lower())

print("Lowercased strings with length > 5:", result)
# Lowercased strings with length > 5: []


# (iii) Write a Python program to print a specified list after removing the 0th, 4th and 5th elements

sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Teapink']

result = []
for i in range(len(sample_list)):
    if i not in [0, 4, 5]:
        result.append(sample_list[i])

print("List after removing 0th, 4th, and 5th elements:", result)
# List after removing 0th, 4th, and 5th elements: ['Green', 'White', 'Black', 'Teapink']