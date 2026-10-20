# ICT105 - Worksheet 4, Session 7 {mon}
def course_enrollment(student_id, first_name, last_name, course_id, course_name, action="Echo"):
    print(f"{action}: Student {student_id} - {first_name} {last_name} has been registered for {course_id}: {course_name}")

print("=== Exercise 1: Student Registration ===")

# Call with positional arguments
course_enrollment(1001, "Alice", "Smith", "CS101", "Introduction to Computer Science")

# Call with keyword argument Add
course_enrollment(1002, "Bob", "Johnson", "MATH101", "Calculus I", action="Add")

# Call with default Echo
course_enrollment(1003, "Charlie", "Brown", "PHY101", "General Physics I")

# Student Action - Amend and Delete
print("\n=== Student Actions ===")
course_enrollment(1004, "David", "Lee", "CS202", "Data Structures and Algorithms", action="Amend")
course_enrollment(1005, "Emily", "Davis", "BIO101", "Biology I", action="Delete")


# ---- EXERCISE 2: Student Course List ----
print("\n=== Exercise 2: Student Course List ===")

def collect_courses():
    courses = []
    print("Enter 4 course IDs:")
    for i in range(4):
        course = input(f"  Course {i+1} ID: ")
        courses.append(course)
    return courses

def course_summary(student_id, student_name):
    print(f"\nBuilding course list for Student {student_id} - {student_name}")
    courses = collect_courses()
    semester = input("Enter semester (e.g. S1): ")
    year = input("Enter year (e.g. 2024): ")
    print(f"\nSummary for {student_name} (ID: {student_id}):")
    for c in courses:
        print(f"  - {c}")
    print(f"Semester: {semester}, Year: {year}")

course_summary(1001, "Alice Smith")

# Dictionary of courses using arbitrary keyword arguments
print("\n=== Course Dictionary ===")

def course_dict(**courses):
    print("Courses enrolled:")
    for course_id, course_name in courses.items():
        print(f"  {course_id}: {course_name}")

course_dict(
    CS101="Introduction to Computer Science",
    MATH101="Calculus I",
    PHY101="General Physics I",
    BIO101="Biology I"
)


# ---- EXERCISE 3: Tkinter Calculator ----
print("\n=== Exercise 3: Tkinter Calculator ===")
print("Opening calculator window...")

import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                result_label.config(text="Error: Division by zero")
                return
            result = num1 / num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Error: Invalid input")

root = tk.Tk()
root.title("Simple Calculator")

tk.Label(root, text="Number 1:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Number 2:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Operation:").grid(row=2, column=0, padx=10, pady=5)
operation = tk.StringVar(value="+")
for i, op in enumerate(["+", "-", "*", "/"]):
    tk.Radiobutton(root, text=op, variable=operation, value=op).grid(row=2, column=i+1)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2, pady=10)
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()


# =============================
# ICT105 - Worksheet 4, Session 8
# =============================

# ---- EXERCISE 1 & 2: User Class ----
print("\n=== Session 8 - Exercise 1 & 2: User Class ===")

class User:
    def __init__(self, first_name, last_name, email, username, date_of_birth, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.date_of_birth = date_of_birth
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nUser Profile:")
        print(f"  Name     : {self.first_name} {self.last_name}")
        print(f"  Email    : {self.email}")
        print(f"  Username : {self.username}")
        print(f"  DOB      : {self.date_of_birth}")
        print(f"  Location : {self.location}")

    def greet_user(self):
        print(f"Welcome back, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# Create instances
user1 = User("Alice", "Smith", "sd1001@uni123st.edu.au", "alice_s", "2000-01-15", "Perth")
user2 = User("Bob", "Johnson", "sd1002@uni123st.edu.au", "bob_j", "1999-05-20", "Sydney")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

# Login attempts
print("\n=== Exercise 2: Login Attempts ===")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"Login attempts for {user1.first_name}: {user1.login_attempts}")
user1.reset_login_attempts()
print(f"After reset, login attempts: {user1.login_attempts}")


# ---- EXERCISE 3: Classroom Class ----
print("\n=== Exercise 3: Classroom ===")

class Classroom:
    def __init__(self, classroom_name, classroom_location, seats_in_class):
        self.classroom_name = classroom_name
        self.classroom_location = classroom_location
        self.seats_in_class = seats_in_class
        self.students_enrolled = 0
        self.enrollment_log = []

    def describe_classroom(self):
        print(f"\nClassroom  : {self.classroom_name}")
        print(f"Location   : {self.classroom_location}")
        print(f"Seats      : {self.seats_in_class}")

    def checksize_classroom(self):
        print(f"{self.classroom_name} has {self.seats_in_class} seats available.")

    # ---- EXERCISE 4: Enrolled Students ----
    def set_number_enrolled(self, number):
        self.students_enrolled = number
        print(f"Students enrolled set to: {self.students_enrolled}")

    def update_number_enrolled(self, number):
        old = self.students_enrolled
        self.students_enrolled = number
        log_entry = f"Changed from {old} to {number}"
        self.enrollment_log.append(log_entry)
        print(f"Updated enrollment: {self.students_enrolled}")
        print(f"Audit log: {self.enrollment_log}")


# Create classroom instances
room1 = Classroom("Room 101", "Ground Floor Building A", 15)
room2 = Classroom("Room 205", "1st Floor Building A", 30)
room3 = Classroom("Room 206", "1st Floor Building A", 40)

print(f"\nClassroom name: {room1.classroom_name}")
print(f"Location: {room1.classroom_location}")
print(f"Seats: {room1.seats_in_class}")
room1.describe_classroom()
room1.checksize_classroom()

room2.describe_classroom()
room3.describe_classroom()

# Exercise 4
print("\n=== Exercise 4: Enrolled Students ===")
print(f"Students enrolled: {room1.students_enrolled}")
room1.students_enrolled = 10
print(f"Updated manually: {room1.students_enrolled}")
room1.set_number_enrolled(15)
room1.update_number_enrolled(12)
room1.update_number_enrolled(14)


# ---- EXERCISE 5: Equipment Class ----
print("\n=== Exercise 5: Classroom Equipment ===")

class Equipment(Classroom):
    def __init__(self, classroom_name, classroom_location, seats_in_class):
        super().__init__(classroom_name, classroom_location, seats_in_class)
        self.devices = [
            "Interactive Whiteboard (IW1)",
            "Desktop Computers (DT1)",
            "Laptops (Lap1)",
            "Tablets (Tab1)",
            "Document Cameras (Cam1)",
            "Smart TVs (STV1)",
            "Sound System (SS1)",
            "Wi-Fi Access Point (AP1)",
            "Charging Stations (CS1)",
            "Digital Signage (DS1)"
        ]

    def display_devices(self):
        print(f"\nDevices in {self.classroom_name}:")
        for device in self.devices:
            print(f"  - {device}")

equipped_room = Equipment("Room 107", "Ground Floor Building A", 30)
equipped_room.describe_classroom()
equipped_room.display_devices()