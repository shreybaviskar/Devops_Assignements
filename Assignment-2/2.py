students = {}

while True:
    print("\n1. Add Student")
    print("2. Update Student")
    print("3. Display Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade

    elif choice == '2':
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
        else:
            print("Student not found")

    elif choice == '3':
        for name, grade in students.items():
            print(name, ":", grade)

    elif choice == '4':
        break

    else:
        print("Invalid choice")