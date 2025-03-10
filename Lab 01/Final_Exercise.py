# This program is a basic student management system that allows adding, viewing, and updating student records.

print("Welcome to the Student Management System!")

students = []  

def add_student(name, age, grades):
    """Function to add a student record."""
    student = {
        'name': name,
        'age': age,
        'grades': grades
    }
    students.append(student)

def view_students():
    """Function to view all students."""
    if not students:
        print("No students in the system.")
    else:
        for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}, Grades: {student['grades']}")

def update_student(name, age=None, grades=None):
    """Function to update a student's record."""
    for student in students:
        if student['name'] == name:
            if age:
                student['age'] = age
            if grades:
                student['grades'] = grades
            print(f"Updated record for {name}.")
            return
    print(f"Student {name} not found.")

def delete_student(name):
    """Function to delete a student by name."""
    for student in students:
        if student['name'] == name:
            students.remove(student)
            print(f"Student {name} has been deleted.")
            return
    print(f"Student {name} not found.")


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        name = input("Enter student's name: ")
        age = int(input("Enter student's age: "))
        grades = input("Enter student's grades (comma separated, Like Math:90, Science:85): ")

        if grades:
            grades_list = grades.split(",")
            grades = []
            for grade in grades_list:
                grades.append(tuple(grade.split(":")))
        else:
            grades = None
            
        grades = [(subject.strip(), int(grade.strip())) for subject, grade in grades]
        add_student(name, age, grades)
        print(f"Student {name} added successfully.")

    elif choice == '2':
        print("\n--- Student Records ---")
        view_students()

    elif choice == '3':
        name = input("Enter the student name to update: ")
        age = input("Enter new age: ")
        grades = input("Enter new grades: ")

        age = int(age) if age else None

        if grades:
            grades_list = grades.split(",")
            grades = []
            for grade in grades_list:
                grades.append(tuple(grade.split(":")))
        else:
            grades = None

        if grades:
            updated_grades = []
            for subject, grade in grades:
                updated_grades.append((subject.strip(), int(grade.strip())))
            grades = updated_grades
        else:
            grades = None

        update_student(name, age, grades)

    elif choice == '4':
        name = input("Enter the student's name to delete: ")
        delete_student(name)

    elif choice == '5':
        print("Exiting program...")
        break

    else:
        print("Invalid choice, please try again.")
