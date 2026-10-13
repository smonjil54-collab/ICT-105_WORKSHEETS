# ICT105 - Worksheet 3, Session 5"
print("=== Student Course Enrollments ===")
course_enrollments = {
    1001: ["CS101", "MATH101"],
    1002: ["CS101", "MATH102"],
    1003: ["CS202", "PHY101"],
    1004: ["CS202", "CHEM101"],
    1005: ["BIO101", "HIST101"],
    1006: ["BIO102", "ENGL101"],
    1007: ["ECON101", "PSY101"],
    1008: ["ECON102", "SOC101"],
    1009: ["PSY102", "SOC102"],
    1010: ["CS101", "MATH101"]
}

for student_id, courses in course_enrollments.items():
    print(f"Student ID {student_id} is enrolled in: {', '.join(courses)}")


# ---- SECTION 2: Class Schedule by Department ----
print("\n=== Class Schedule by Department ===")
departments = {
    "Computer Science": [("Computer Science", "CS101", "Introduction to Computer Science"),
                         ("Computer Science", "CS202", "Data Structures and Algorithms")],
    "Mathematics":      [("Mathematics", "MATH101", "Calculus I"),
                         ("Mathematics", "MATH102", "Calculus II")],
    "Physics":          [("Physics", "PHY101", "General Physics I"),
                         ("Physics", "PHY102", "General Physics II")],
    "Chemistry":        [("Chemistry", "CHEM101", "General Chemistry I"),
                         ("Chemistry", "CHEM102", "General Chemistry II")],
    "Biology":          [("Biology", "BIO101", "Biology I"),
                         ("Biology", "BIO102", "Biology II")],
    "History":          [("History", "HIST101", "American History I"),
                         ("History", "HIST102", "American History II")],
    "English":          [("English", "ENGL101", "English Composition I"),
                         ("English", "ENGL102", "English Composition II")],
    "Economics":        [("Economics", "ECON101", "Principles of Economics"),
                         ("Economics", "ECON102", "Intermediate Microeconomics")],
    "Psychology":       [("Psychology", "PSY101", "Introduction to Psychology"),
                         ("Psychology", "PSY102", "Developmental Psychology")],
    "Sociology":        [("Sociology", "SOC101", "Introduction to Sociology"),
                         ("Sociology", "SOC102", "Social Problems")]
}

for dept, courses in departments.items():
    print(f"\nDepartment: {dept}")
    for course in courses:
        print(f"  - [{course[1]}] {course[2]}")


# ---- SECTION 3: Lecturer Assignments ----
print("\n=== Lecturer Assignments ===")
lecturer_assignments = {
    "Dr. Emily Brown":        ["CS101", "MATH102"],
    "Mr. Michael Johnson":    ["CS202", "PHY102"],
    "Asst. Prof. Olivia Taylor": ["MATH101", "CHEM101"],
    "Miss. Sophia Carter":    ["CHEM102", "BIO101", "BIO102"],
    "Dr. Oliver Hernandez":   ["HIST101", "HIST102", "ENGL101"],
    "Prof. Isabella Garcia":  ["ENGL102", "SOC101"],
    "Prof. Evelyn Russell":   ["ECON101", "ECON102"],
    "Dr. Lucas Sanchez":      ["PSY101", "PSY102"],
    "Asst. Prof. Liam Lopez": ["SOC102"],
    "Prof. David Lee":        ["PHY101"]
}

for lecturer, courses in lecturer_assignments.items():
    print(f"{lecturer} teaches: {', '.join(courses)}")


# =============================
# ICT105 - Worksheet 3, Session 6
# =============================

# ---- SECTION 1: User Input Loop - Build Class List ----
print("\n=== Build Class List ===")
class_list = []
print("Enter student names one by one. Type 'done' when finished.")
while True:
    name = input("Enter student name: ")
    if name.lower() == "done":
        break
    class_list.append(name)
    print(f"{name} has been added to the class.")

print("\nClass list:")
for student in class_list:
    print(f" - {student}")


# ---- SECTION 2: Find Rooms by Capacity ----
print("\n=== Room Finder ===")
rooms = [
    {"room": 101, "capacity": 15, "floor": "Ground Floor", "location": "Building A"},
    {"room": 102, "capacity": 15, "floor": "Ground Floor", "location": "Building A"},
    {"room": 103, "capacity": 20, "floor": "Ground Floor", "location": "Building A"},
    {"room": 104, "capacity": 20, "floor": "Ground Floor", "location": "Building A"},
    {"room": 105, "capacity": 25, "floor": "Ground Floor", "location": "Building A"},
    {"room": 106, "capacity": 25, "floor": "Ground Floor", "location": "Building A"},
    {"room": 107, "capacity": 30, "floor": "Ground Floor", "location": "Building A"},
    {"room": 108, "capacity": 30, "floor": "Ground Floor", "location": "Building A"},
    {"room": 201, "capacity": 10, "floor": "1st Floor",    "location": "Building A"},
    {"room": 206, "capacity": 40, "floor": "1st Floor",    "location": "Building A"},
]

min_seats = int(input("Enter minimum number of seats needed: "))
print("\nRooms that can accommodate your class:")
found = False
for room in rooms:
    if room["capacity"] >= min_seats:
        print(f" - Room {room['room']}: Capacity {room['capacity']}, {room['floor']}, {room['location']}")
        found = True
if not found:
    print("No rooms found with that capacity.")


# ---- SECTION 3a: Exit with quit/exit/0 ----
print("\n=== Class List with Exit Option ===")
students_a = []
print("Enter student names. Type 'quit', 'exit' or '0' to stop.")
while True:
    name = input("Enter student name: ")
    if name.lower() in ["quit", "exit", "0"]:
        print(f"\nExited using '{name}'")
        print(f"Total students entered: {len(students_a)}")
        for s in students_a:
            print(f" - {s}")
        break
    students_a.append(name)
    print(f"{name} has been added.")


# ---- SECTION 3b: Active Variable to Control Loop ----
print("\n=== Active Variable Loop ===")
students_b = []
active = True
print("Enter student names. Type 'stop' to end.")
while active:
    name = input("Enter student name: ")
    if name.lower() == "stop":
        active = False
    else:
        students_b.append(name)
        print(f"{name} has been added.")

print("\nFinal class list:")
for s in students_b:
    print(f" - {s}")


# ---- SECTION 3c: Break on Max Capacity ----
print("\n=== Max Capacity Loop ===")
students_c = []
max_cap = 5  # maximum students allowed
print(f"Enter student names. Max capacity is {max_cap} students.")
while True:
    name = input("Enter student name: ")
    students_c.append(name)
    print(f"{name} has been added.")
    if len(students_c) >= max_cap:
        print(f"\nMax capacity of {max_cap} reached!")
        print("Students in class:")
        for s in students_c:
            print(f" - {s}")
        break


# ---- SECTION 4: Infinite Loop (press CTRL+C to exit) ----
print("\n=== Infinite Input Loop (press CTRL+C to exit) ===")
lines = []
try:
    while True:
        entry = input("Enter text: ")
        lines.append(entry)
        print(entry)
except KeyboardInterrupt:
    print(f"\nTotal lines entered: {len(lines)}")