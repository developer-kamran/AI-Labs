# # I. You have collected information about cities in your province. You decide to store each city’s
# # name, population, and mayor in a file. Write a python program to accept the data for a number
# # of cities from the keyboard and store the data in a file in the order in which they’re entered

def save_city_data(filename="cities.txt"):
    with open(filename, "w") as file:
        while True:
            city = input("Enter city name (or 'exit' to stop): ")
            if city.lower() == "exit":
                break
            population = input("Enter population: ")
            mayor = input("Enter mayor's name: ")
            
            file.write(f"{city}, {population}, {mayor}\n")
    
    print(f"Data saved to {filename}")

save_city_data()


# II. Write a python program to create a data file student.txt and append the message “Now we are
# AI students”s

def append_message(filename="student.txt"):
    with open(filename, "a") as file:  # "a" mode appends data without overwriting
        file.write("Now we are AI students\n")
    
    print(f'Message appended to {filename}')

append_message()