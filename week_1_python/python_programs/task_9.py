# list
students = []

# function to add student
def add_student():
    print("\n---Add Student---")
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    branch = input("Enter branch: ")
    age = int(input("Enter age: "))

    student = {
        "name": name,
        "roll_number": roll_number,
        "branch": branch,
        "age": age
    }

    students.append(student)

    print("Student record added successfully!")

# function to display all students
def display_students():
    print("\n---All Students---")
    if not students:
        print("No student records found.")
        return

    for student in students:
        print(f"Name: {student['name']}")
        print(f"Roll Number: {student['roll_number']}")
        print(f"Branch: {student['branch']}")
        print(f"Age: {student['age']}")    

# function to search for a student by name
def search_student():
    print("\n---Search Student---")
    search_name = input("Enter student name to search: ").strip()

    found = False

    for student in students:
        if student["name"].lower() == search_name.lower():
            print("\nStudent Found:")
            print(f"Name: {student['name']}")
            print(f"Roll Number: {student['roll_number']}")
            print(f"Branch: {student['branch']}")
            print(f"Age: {student['age']}")
            found = True

    if not found:
        print("Student not found")

# function to delete a student by roll number
def delete_student():
    print("\n---Delete Student---")
    roll_number = input("Enter roll number to delete: ").strip()

    for student in students:
        if student["roll_number"] == roll_number:
            students.remove(student)
            print("Student record deleted successfully!")
            return

    print("Student record not found")


while True:
    print("\n---Student Record Management System---")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by Name")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Exiting Student Record Management System. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 5.")