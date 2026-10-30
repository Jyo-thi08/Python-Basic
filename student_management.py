students = []

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    marks = []

    for i in range(1, 4):
        mark = float(input(f"Enter subject {i} marks: "))
        marks.append(mark)

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")


def display_students():
    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:
        total = sum(student["marks"])
        percentage = total / 3

        print("\nStudent Name:", student["name"])
        print("Roll Number:", student["roll_no"])
        print("Total Marks:", total)
        print("Percentage:", percentage, "%")

        if all(mark >= 35 for mark in student["marks"]):
            print("Result: PASS")
        else:
            print("Result: FAIL")


def highest_scorer():
    if len(students) == 0:
        print("No records available.")
        return

    top_student = max(
        students,
        key=lambda s: sum(s["marks"])
    )

    print("Highest Scorer:", top_student["name"])
    print("Total Marks:", sum(top_student["marks"]))


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Find Highest Scorer")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        highest_scorer()

    elif choice == "4":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice! Try again.")
