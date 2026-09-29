
# ICT105 - Worksheet 2, Session 3
courses = [
    "Physics I",
    "Introduction to Programming",
    "Calculus I",
    "Biology I",
    "Data Structures and Algorithms",
    "Microeconomics",
    "Linear Algebra",
    "English Composition I",
    "Chemistry I",
    "Psychology I",
    "History I",
    "Macroeconomics",
    "Introduction to Philosophy",
    "Calculus II",
    "Discrete Mathematics"
]

print("=== Original List ===")
print(courses)

# ---- SECTION 2: Lists - sorted() ----
print("\n=== Sorted Alphabetically (sorted) ===")
print(sorted(courses))

print("\n=== Sorted Reverse Alphabetically (sorted reverse) ===")
print(sorted(courses, reverse=True))

# ---- SECTION 3: Lists - reverse() ----
courses.reverse()
print("\n=== After reverse() ===")
print(courses)

courses.reverse()
print("\n=== After reverse() again ===")
print(courses)

# ---- SECTION 4: Lists - sort() ----
courses.sort()
print("\n=== After sort() Alphabetically ===")
print(courses)

courses.sort(reverse=True)
print("\n=== After sort() Reverse Alphabetically ===")
print(courses)

# ---- SECTION 2.1: Lists - Useable Coding ----

# Reset list to original order
courses = [
    "Physics I",
    "Introduction to Programming",
    "Calculus I",
    "Biology I",
    "Data Structures and Algorithms",
    "Microeconomics",
    "Linear Algebra",
    "English Composition I",
    "Chemistry I",
    "Psychology I",
    "History I",
    "Macroeconomics",
    "Introduction to Philosophy",
    "Calculus II",
    "Discrete Mathematics"
]

# Exercise 1 - Announce available courses
sorted_courses = sorted(courses)
print("\n=== Available Courses ===")
print("The following courses are available for expression of interest if the students meet the prerequisites:")
for course in sorted_courses:
    print(" -", course)

# Exercise 2 - Replace a course
withdrawn = "Macroeconomics"
new_course = "Statistics I"
index = courses.index(withdrawn)
courses[index] = new_course
print(f"\n=== Course Update ===")
print(f"NOTICE: '{withdrawn}' has been withdrawn.")
print(f"NOTICE: '{new_course}' has been added as a replacement.")
print("Updated course list:")
for course in courses:
    print(" -", course)

# Exercise 3 - Add 3 more courses
courses.insert(0, "Organic Chemistry")           # beginning
courses.insert(len(courses)//2, "World History") # middle
courses.append("Introduction to Sociology")      # end
print("\n=== 3 New Courses Added ===")
for course in courses:
    print(" -", course)

# Exercise 4 - Remove 4 courses
removed = []
for _ in range(4):
    removed.append(courses.pop())
print("\n=== Course Removal Notice ===")
print("The following courses are unavailable due to technical and room availability issues:")
for r in removed:
    print(f" - {r} has been withdrawn.")
print("\nRemaining available courses:")
for course in courses:
    print(" -", course)

# ---- SECTION 3: Tuples and Loops ----
print("\n=== Tuples and Loops ===")
course_tuples = [
    (1, "Introduction to Programming"),
    (2, "Calculus I"),
    (3, "Data Structures and Algorithms"),
    (4, "Linear Algebra"),
    (5, "Physics I"),
    (6, "Chemistry I"),
    (7, "Biology I"),
    (8, "Microeconomics"),
    (9, "Macroeconomics"),
    (10, "Psychology I"),
    (11, "History I"),
    (12, "English Composition I"),
    (13, "Introduction to Philosophy"),
    (14, "Calculus II"),
    (15, "Discrete Mathematics")
]

course_list = []
for course_id, course_name in course_tuples:
    course_list.append(course_name)

print("Course Information:")
for i, name in enumerate(course_list):
    print(f" ID {i+1}: {name}")


# =============================
# ICT105 - Worksheet 2, Session 4
# =============================

# ---- SECTION 5.2: Conditional Statements - Department Search ----
print("\n=== Department Search ===")
departments = [
    [1, "Computer Science"],
    [2, "Mathematics"],
    [3, "Computer Science"],
    [4, "Mathematics"],
    [5, "Physics"],
    [6, "Chemistry"],
    [7, "Biology"],
    [8, "Economics"],
    [9, "Economics"],
    [10, "Psychology"],
    [11, "History"],
    [12, "English"],
    [13, "Philosophy"],
    [14, "Mathematics"],
    [15, "Computer Science"]
]

while True:
    user_input = input("\nEnter a Course ID (1-15), or 'quit' / '0' to exit: ")

    if user_input.lower() == "quit":
        print(f"The value '{user_input}' has been used to exit.")
        break

    if not user_input.isdigit():
        print("Please enter a valid number or 'quit'.")
        continue

    course_id = int(user_input)

    if course_id == 0:
        print("Course ID is out of range (1-15), try again.")
        continue

    found = False
    for dept in departments:
        if dept[0] == course_id:
            print(f"Course ID {course_id} is in the {dept[1]} department.")
            found = True
            break

    if not found:
        if course_id > 15:
            print("Course ID is out of range (1-15), try again.")
        else:
            print(f"Course ID {course_id} not found.")


# ---- SECTION 5.3: Course Information Retrieval System ----
print("\n=== Course Information Retrieval System ===")
course_data = [
    [1, "Introduction to Programming", "Computer Science", "None"],
    [2, "Calculus I", "Mathematics", "None"],
    [3, "Data Structures and Algorithms", "Computer Science", "Introduction to Programming"],
    [4, "Linear Algebra", "Mathematics", "None"],
    [5, "Physics I", "Physics", "None"],
    [6, "Chemistry I", "Chemistry", "None"],
    [7, "Biology I", "Biology", "None"],
    [8, "Microeconomics", "Economics", "None"],
    [9, "Macroeconomics", "Economics", "Microeconomics"],
    [10, "Psychology I", "Psychology", "None"],
    [11, "History I", "History", "None"],
    [12, "English Composition I", "English", "None"],
    [13, "Introduction to Philosophy", "Philosophy", "None"],
    [14, "Calculus II", "Mathematics", "Calculus I"],
    [15, "Discrete Mathematics", "Computer Science", "Introduction to Programming"]
]

while True:
    user_input = input("\nEnter a Course ID (1-15) to retrieve info, or '0' to quit: ")

    if not user_input.isdigit():
        print("Invalid input. Please enter a number.")
        continue

    course_id = int(user_input)

    if course_id == 0:
        print("Exiting Course Retrieval System.")
        break

    found = False
    for course in course_data:
        if course[0] == course_id:
            print(f"\nCourse Name   : {course[1]}")
            print(f"Department    : {course[2]}")
            print(f"Prerequisites : {course[3]}")
            found = True
            break

    if not found:
        print(f"Course ID {course_id} not found. Please try again.")
