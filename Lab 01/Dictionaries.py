# (i) Use dir and help to learn about the functions you can call on dictionaries and implement it. 
dict = {'Ahsan': 29, 'Mustafa': 24, 'Arham': 16}

copied_dict = dict.copy()
print("Copy of dictionary:", copied_dict)
# Copy of dictionary: {'Ahsan': 29, 'Mustafa': 24, 'Arham': 16}
 
new_dict = dict.fromkeys(['Arham', 'Mustafa', 'Ahsan'], 3.6) # Create a new dictionary with keys and a default value
print("From keys:", new_dict)
# From keys: {'Arham': 3.6, 'Mustafa': 3.6, 'Ahsan': 3.6}

value = dict.get('Rahim', 'Not Found') # Get the value for a key, with a default value if the key doesn't exist
print("Value for key 'b': ", value)
# Value for key 'b': Not Found

print("Items in dictionary:", dict.items())
# Items in dictionary: dict_items([('Ahsan', 29), ('Mustafa', 24), ('Arham', 16)])

print("Keys in dictionary:", dict.keys())
# Keys in dictionary: dict_keys(['Ahsan', 'Mustafa', 'Arham'])

pop_value = dict.pop('Suleman', 'Key not found')
print("After pop('c'):", dict)
# After pop('c'): {'Ahsan': 29, 'Mustafa': 24, 'Arham': 16}
print("Popped value:", pop_value)
# Popped value: Key not found

last_item = dict.popitem() #Remove and return the last key-value pair
print("After popitem:", dict)
# After popitem: {'Ahsan': 29, 'Mustafa': 24}
print("Last item:", last_item)
# Last item: ('Arham', 16)

# remaking the dictionary
dict = {'Kamran': 21, 'Abdullah': 19, 'Huzaifa': 21}

default_value = dict.setdefault('Zawad', 19)
print("After setdefault:", dict)
# After setdefault: {'Kamran': 21, 'Abdullah': 19, 'Huzaifa': 21, 'Zawad': 19}

dict.update({'Wajahat': 20, 'Zafar': 21})
print("After update:", dict)
# After update: {'Kamran': 21, 'Abdullah': 19, 'Huzaifa': 21, 'Zawad': 19, 'Wajahat': 20, 'Zafar': 21}

dict.clear()
print("After clear():", dict)
# After clear(): {}


# (ii) Write a Python script to concatenate following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result = {**dic1, **dic2, **dic3}

print("Concatenated Dictionary:", result)
# Concatenated Dictionary: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
