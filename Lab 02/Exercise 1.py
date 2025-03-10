# # EXERCISE 1:

# (I) Cabinets and Boxes are objects that are mostly in cubic shape. Make a program that takes
# inputs like height, width and depth from user and then calculate volume of the cube:
# volume = height ∗ width ∗ depth

def categorize_volume(volume):
    if 1 <= volume <= 10:
        return "Extra Small"
    elif 11 <= volume <= 25:
        return "Small"
    elif 26 <= volume <= 75:
        return "Medium"
    elif 76 <= volume <= 100:
        return "Large"
    elif 101 <= volume <= 250:
        return "Extra Large"
    else:
        return "Extra-Extra Large"

def main():
    try:
        height = float(input("Enter height (cm): "))
        width = float(input("Enter width (cm): "))
        depth = float(input("Enter depth (cm): "))
        
        volume = height * width * depth
        label = categorize_volume(volume)
        
        print(f"Volume: {volume} cm³")
        print(f"Category: {label}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()



# (II) In a company ,worker efficiency is determined on the basis of the time required for a worker
# to complete a particular job.If the time taken by the worker is between 2-3 hours then the worker
# is said to be highly efficient. If the time required by the worker is between 3-4hours,then the worker
# is ordered to improve speed. If the time taken is between 4-5 hours ,the worker is given training to
# improve his speed ,and if the time taken by the worker is more than 5 hours ,then the worker haas
# to leave the company, If the time taken by the worker is input through the keyboard,find the
# efficiency of the worker.

def evaluate_efficiency(time_taken):
    if 2 <= time_taken < 3:
        return "Highly Efficient"
    elif 3 <= time_taken < 4:
        return "Improve Speed"
    elif 4 <= time_taken < 5:
        return "Training Required"
    else:
        return "Worker must leave the company"
  
if __name__ == "__main__":
    time_taken = float(input("Enter time taken (hours): "))
    efficiency = evaluate_efficiency(time_taken)
    print(f"Efficiency: {efficiency}")



# (iii) The program must prompt the user for a username and password. The program should
# compare the password given by the user to a known password. If the password matches, the
# program should display “Welcome!” If it doesn’t match, the program should display “I don’t
# know you.

def authenticate_user():
    
    username = input("Enter your username: ")
    password = input("Enter your password: ").strip()
    
    if password.lower() == "abc$123".lower() :
        print("Welcome!")
    else:
        print("I don't know you.")

if __name__ == "__main__":
    authenticate_user()

