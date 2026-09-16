students = []


def add_student():
    name = input("Enter student name: ").strip()
    age = input("Enter student age: ").strip()
    branch = input("Enter student branch: ").strip()
    students.append({"name": name, "age": age, "branch": branch})
    print("Student added successfully.")


def display_students():
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for index, student in enumerate(students, start=1):
        print(
            f"{index}. Name: {student['name']}, "
            f"Age: {student['age']}, Branch: {student['branch']}"
        )


def search_student():
    search_name = input("Enter the name to search: ").strip().lower()
    matches = [
        student for student in students
        if search_name in student["name"].lower()
    ]

    if not matches:
        print("Student not found.")
        return

    for student in matches:
        print(
            f"Name: {student['name']}, "
            f"Age: {student['age']}, Branch: {student['branch']}"
        )


def delete_student():
    delete_name = input("Enter the name to delete: ").strip().lower()
    for index, student in enumerate(students):
        if student["name"].lower() == delete_name:
            students.pop(index)
            print("Student deleted successfully.")
            return
    print("Student not found.")


def main():
    while True:
        print("\nStudent Record Management System")
        print("1. Add student")
        print("2. Display all students")
        print("3. Search student")
        print("4. Delete student")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()
