# Random Module
import random

#gnerate a random integer between 50 and 100
print("Random integer between 50 and 100:", random.randint(50, 100))

#generate a random floating-point number between 1.5 and 7.5
print("Random float between 1.5 and 7.5:", random.uniform(1.5, 7.5))

#choose random element from list
colors = ["Red", "Blue", "Green", "Yellow", "Purple"]
random_color = random.choice(colors)
print("Randomly chosen color:", random_color)

#shuffle deck of cards 
deck = list(range(1, 53))
random.shuffle(deck)
print("Shuffled deck:", deck[:10])  #will show first 10 cards

#randomly picks 5 lottery numbers from 1 to 50
lottery_numbers = random.sample(range(1, 51), 5)
print("Lottery numbers:", lottery_numbers)


# Time Module
import time

current_time = time.time()
print("Current time in seconds since epoch:", current_time)

# Convert the time to a human-readable string
print("Human-readable time:", time.ctime(current_time))

# Pause the execution for 3 seconds
print("Pausing for 3 seconds...")
time.sleep(3)
print("Resumed execution.")
