# =====================================================================
# ICT105 - Worksheet 5 (Sessions 9 & 10) - all exercises in ONE file
# Run:  python ICT105_Worksheet5_All.py
# Pick an exercise from the menu. Session 10 needs: pip install requests plotly
# =====================================================================
import csv
import json
import logging
import re
import time
from pathlib import Path
import requests

STUDENTS = """1001,Alice,Smith,sd1001@uni123st.edu.au
1002,Bob,Johnson,sd1002@uni123st.edu.au
1003,Charlie,Brown,sd1003@uni123st.edu.au
1004,David,Lee,sd1004@uni123st.edu.au
1005,Emily,Davis,sd1005@uni123st.edu.au
1006,Frank,Wilson,sd1006@uni123st.edu.au
1007,Grace,Taylor,sd1007@uni123st.edu.au
1008,Henry,Anderson,sd1008@uni123st.edu.au
1009,Isabella,Thomas,sd1009@uni123st.edu.au
1010,Jack,Hill,sd1010@uni123st.edu.au
1011,Kate,Baker,sd1011@uni123st.edu.au
1012,Liam,Carter,sd1012@uni123st.edu.au
1013,Maria,Evans,sd1013@uni123st.edu.au
1014,Noah,Robinson,sd1014@uni123st.edu.au
1015,Olivia,Lewis,sd1015@uni123st.edu.au
1016,Parker,Allen,sd1016@uni123st.edu.au
1017,Quinn,Williams,sd1017@uni123st.edu.au
1018,Riley,Jones,sd1018@uni123st.edu.au
1019,Sophia,Clark,sd1019@uni123st.edu.au
1020,Tyler,Brown,sd1020@uni123st.edu.au
"""


def ensure_students_csv():
    """Create students.csv from the sample data if it does not exist."""
    if not Path("students.csv").exists():
        Path("students.csv").write_text(STUDENTS)


# ---------------------------------------------------------------------
# SESSION 9
# ---------------------------------------------------------------------
class FileHandler:
    """Exercise 1: create a text file and read it two ways, with error handling."""

    def __init__(self, filename):
        self.filename = filename

    def create_file(self):
        lines = [
            "Python is a high-level, readable programming language.\n",
            "I have learned about variables, loops and functions.\n",
            "Error handling uses try-except blocks.\n",
            "Debugging can use print statements, logging and pdb.\n",
        ]
        try:
            with open(self.filename, "w") as f:
                f.writelines(lines)
            print(f"File '{self.filename}' created.")
        except PermissionError:
            print(f"Permission denied: cannot write to '{self.filename}'.")

    def read_whole_file(self):
        try:
            with open(self.filename, "r") as f:
                print("--- (a) Whole file at once ---")
                print(f.read())
        except FileNotFoundError:
            print(f"Error: '{self.filename}' was not found.")
        except PermissionError:
            print(f"Permission denied: cannot read '{self.filename}'.")

    def read_line_by_line(self):
        try:
            with open(self.filename, "r") as f:
                lines = f.readlines()
            print("--- (b) Line by line ---")
            for number, line in enumerate(lines, start=1):
                print(f"Line {number}: {line.strip()}")
        except FileNotFoundError:
            print(f"Error: '{self.filename}' was not found.")
        except PermissionError:
            print(f"Permission denied: cannot read '{self.filename}'.")

    def read_csv_lines(self):
        try:
            with open(self.filename, newline="") as f:
                for row in csv.reader(f):
                    print(row)
        except FileNotFoundError:
            print(f"Error: '{self.filename}' was not found.")


def s9_ex1():
    handler = FileHandler("python_summary.txt")
    handler.create_file()
    handler.read_whole_file()
    handler.read_line_by_line()
    print("\n--- students.csv ---")
    FileHandler("students.csv").read_csv_lines()
    print("\n--- Missing file test ---")
    FileHandler("does_not_exist.txt").read_whole_file()


def s9_ex2():
    # a) Create the input file
    content = (
        "Every learner must complete their assignments on time.\n"
        "A good learner always seeks to learn more.\n"
        "Learners are the future leaders.\n"
    )
    with open("learning_students.txt", "w") as f:
        f.write(content)

    # b) Replace learner(s) with student(s), keeping capital letters
    def swap(match):
        return "Student" if match.group(0)[0].isupper() else "student"

    try:
        with open("learning_students.txt", "r") as f:
            for line in f:
                print(re.sub(r"learner", swap, line.rstrip("\n"), flags=re.IGNORECASE))
    except FileNotFoundError:
        print("Error: learning_students.txt was not found.")


def s9_ex3():
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(f"The sum of {a} + {b} = {a + b}")
    except ValueError:
        print("Please enter numbers only (e.g. 5 or 12).")
    # Test 1: 4 and 6 -> 10.  Test 2: 4 and abc -> friendly error message.


def s9_ex4():
    print("Simple Adding Calculator (type 'q' at any prompt to quit)")
    while True:
        first = input("\nFirst number: ")
        if first.lower() == "q":
            break
        second = input("Second number: ")
        if second.lower() == "q":
            break
        try:
            print(f"Total: {float(first) + float(second)}")
        except ValueError:
            print("That was not a number. Please enter numbers only and try again.")
    print("Goodbye!")


def s9_ex5_split():
    """Split students.csv into students_c1.txt and students_c2.txt."""
    with open("students.csv", newline="") as f:
        rows = list(csv.reader(f))
    half = len(rows) // 2
    for filename, part in (("students_c1.txt", rows[:half]), ("students_c2.txt", rows[half:])):
        with open(filename, "w") as out:
            for row in part:
                out.write(",".join(row) + "\n")
    print("students.csv split into students_c1.txt and students_c2.txt")


def s9_ex5_ab():
    # a) Read both files; b) move one away and re-run to see the friendly message
    for filename in ("students_c1.txt", "students_c2.txt"):
        try:
            with open(filename, "r") as f:
                print(f"--- {filename} ---")
                print(f.read())
        except FileNotFoundError:
            print(f"Friendly message: '{filename}' could not be found. Please check the folder.")


def s9_ex5_c():
    # c) Missing file is handled silently; the error goes to error.log
    logging.basicConfig(
        filename="error.log",
        level=logging.ERROR,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    for filename in ("students_c1.txt", "students_c2.txt"):
        try:
            with open(filename, "r") as f:
                print(f.read())
        except FileNotFoundError:
            logging.error(f"File not found: {filename}")
    print("(Done. Check error.log for any missing-file entries.)")


def s9_ex6():
    FILENAME = "favourite_number.json"
    # a) Prompt and save with json.dumps()
    try:
        number = int(input("Enter your favourite number: "))
    except ValueError:
        print("Please enter a whole number.")
        return
    with open(FILENAME, "w") as f:
        f.write(json.dumps(number))
    # b) Read back and display
    with open(FILENAME, "r") as f:
        saved = json.loads(f.read())
    print(f"I know your favourite number! It is {saved}.")


def s9_ex7():
    FILENAME = "favourite_number_remembered.json"

    def get_stored_number():
        try:
            with open(FILENAME, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    def get_new_number():
        while True:
            try:
                number = int(input("What is your favourite number? "))
                break
            except ValueError:
                print("Please enter a whole number.")
        with open(FILENAME, "w") as f:
            json.dump(number, f)
        return number

    number = get_stored_number()
    if number is not None:
        print(f"I remember! Your favourite number is {number}.")
    else:
        number = get_new_number()
        print(f"Thanks! I'll remember that your favourite number is {number}.")
    # Run this option twice: 1st run asks, 2nd run reports the stored number.
    # Delete favourite_number_remembered.json to start again.


def s9_ex8():
    FILENAME = "user_profile.txt"
    # a) Collect the student ID and save with json.dump()
    profile = {"student_id": input("Enter your student ID: ").strip()}
    with open(FILENAME, "w") as f:
        json.dump(profile, f)
    # b) Load with json.load()
    with open(FILENAME, "r") as f:
        profile = json.load(f)
    print("Loaded:", profile)
    # c) Add DOB and email, write back
    profile["dob"] = input("Enter your date of birth (DD/MM/YYYY): ").strip()
    profile["email"] = input("Enter your email address: ").strip()
    with open(FILENAME, "w") as f:
        json.dump(profile, f, indent=4)
    # d) Summary report
    with open(FILENAME, "r") as f:
        data = json.load(f)
    print("\n===== Student Summary Report =====")
    print(f"Student ID    : {data['student_id']}")
    print(f"Date of Birth : {data['dob']}")
    print(f"Email         : {data['email']}")
    print("==================================")


def s9_ex9():
    """remember_me.py logic (a: Path + json already imported at the top)."""
    path = Path("username.json")

    def load_username():
        if path.exists():
            try:
                return json.loads(path.read_text())
            except json.JSONDecodeError:
                return None
        return None

    stored = load_username()          # b) check for a stored username
    status = "saved"
    if stored:
        # c) ask whether the current user is the stored user
        if input(f"Are you {stored}? (y/n): ").strip().lower() == "y":
            current = stored
        else:
            while True:
                current = input("What is your name? ").strip()
                if not current:
                    print("Name cannot be empty.")
                elif current.lower() == stored.lower():
                    print("That username already exists. Please choose a different one.")
                else:
                    break
        status = "updated"
    else:
        while True:
            current = input("What is your name? ").strip()
            if current:
                break
            print("Name cannot be empty.")

    path.write_text(json.dumps(current))             # d) store / overwrite
    print(f"Username '{current}' has been {status}.")  # e) confirm


# ---------------------------------------------------------------------
# SESSION 10  (pip install requests plotly)
# ---------------------------------------------------------------------
GITHUB_URL = "https://api.github.com/search/repositories?q=language:python+sort:stars"
HEADERS = {"Accept": "application/vnd.github.v3+json"}


def s10_ex1():
    response = requests.get(GITHUB_URL, headers=HEADERS, timeout=10)
    print(f"Status code: {response.status_code}")
    data = response.json()
    print("\nTop 5 repositories:")
    for repo in data["items"][:5]:
        print(f"- {repo['name']} ({repo['stargazers_count']} stars)")


def s10_ex3():
    import requests
    try:
        response = requests.get(GITHUB_URL, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            response_dict = response.json()
            print(f"Total repositories found: {response_dict['total_count']}")
        else:
            print(f"Request failed with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")


def s10_ex4():
    import requests
    import plotly.express as px

    try:
        response = requests.get(GITHUB_URL, headers=HEADERS, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return

    # d) Handle hitting the rate limit
    if response.status_code in (403, 429):
        reset = int(response.headers.get("X-RateLimit-Reset", 0))
        wait = max(reset - int(time.time()), 0)
        print(f"Rate limit reached. Try again in about {wait} seconds.")
        return
    if response.status_code != 200:
        print(f"Request failed: {response.status_code}")
        return

    # a) remaining = requests left in this window; reset = when the window resets
    print("Requests remaining:", response.headers.get("X-RateLimit-Remaining"))
    print("Limit resets at (epoch):", response.headers.get("X-RateLimit-Reset"))

    repos = response.json()["items"][:10]
    repo_names = [r["name"] for r in repos]
    stars = [r["stargazers_count"] for r in repos]

    # b) Basic bar chart
    px.bar(x=repo_names, y=stars).show()

    # c) Custom title and axis labels
    fig = px.bar(
        x=repo_names,
        y=stars,
        title="Most-Starred Python Repositories on GitHub",
        labels={"x": "Repository", "y": "Stars"},
    )
    fig.update_layout(title_font_size=24, xaxis_title="Repository", yaxis_title="Stars")
    fig.show()


def s10_written_answers():
    print("""
SESSION 10 - WRITTEN ANSWERS

Ex1 a) An API is a set of rules that lets one program request data/services from
       another over the web. Your program calls a URL (endpoint) and gets back
       structured data, usually JSON or CSV.
Ex1 b) https://api.github.com/search/repositories?q=language:python+sort:stars
       https://                 secure protocol
       api.github.com           GitHub's API server (host)
       /search/repositories     endpoint: search repositories
       ?                        start of the query string
       q=                       the search query parameter
       language:python          only repositories written in Python
       +                        separator (space) between search terms
       sort:stars               sort results by number of stars
Ex1 c) pip install requests

Ex2 a) python -m venv .venv
Ex2 b) Windows PowerShell:  .venv\\Scripts\\Activate.ps1
       macOS/Linux:         source .venv/bin/activate
Ex2 c) pip freeze > requirements.txt   (share the file with collaborators)
Ex2 d) pip install -r requirements.txt

Ex4 a) remaining = requests you can still make in the current time window.
       reset     = time (Unix epoch) when the window resets and your allowance returns.
Ex4 c) fig = px.bar(x=repo_names, y=stars, title="My Title",
                    labels={"x": "Repository", "y": "Stars"})
       (or fig.update_layout(title=..., xaxis_title=..., yaxis_title=...))
Ex4 d) Check for status 403/429 and the X-RateLimit-Remaining header. When it is 0,
       read X-RateLimit-Reset, wait (time.sleep) until then and retry. Also make fewer
       calls, cache results, and use a personal access token for a higher limit.
""")


# ---------------------------------------------------------------------
# MENU
# ---------------------------------------------------------------------
MENU = {
    "1":  ("Session 9  - Exercise 1 (file handling class)", s9_ex1),
    "2":  ("Session 9  - Exercise 2 (replace learner)", s9_ex2),
    "3":  ("Session 9  - Exercise 3 (add two numbers)", s9_ex3),
    "4":  ("Session 9  - Exercise 4 (calculator)", s9_ex4),
    "5":  ("Session 9  - Exercise 5: split students.csv into 2 files", s9_ex5_split),
    "5a": ("Session 9  - Exercise 5 a/b: read both files (friendly message)", s9_ex5_ab),
    "5c": ("Session 9  - Exercise 5 c: read both files (log to error.log)", s9_ex5_c),
    "6":  ("Session 9  - Exercise 6 (favourite number, JSON)", s9_ex6),
    "7":  ("Session 9  - Exercise 7 (remember number - run twice)", s9_ex7),
    "8":  ("Session 9  - Exercise 8 (user profile JSON)", s9_ex8),
    "9":  ("Session 9  - Exercise 9 (remember_me)", s9_ex9),
    "10": ("Session 10 - Exercise 1 (GitHub top 5 repos)", s10_ex1),
    "11": ("Session 10 - Exercise 3 (total_count + status check)", s10_ex3),
    "12": ("Session 10 - Exercise 4 (Plotly chart + rate limit)", s10_ex4),
    "13": ("Session 10 - Written answers (Ex 1, 2, 4)", s10_written_answers),
}

if __name__ == "__main__":
    ensure_students_csv()
    while True:
        print("\n===== ICT105 Worksheet 5 =====")
        for key, (title, _) in MENU.items():
            print(f"{key:>3}. {title}")
        print("  q. Quit")
        choice = input("Choose: ").strip().lower()
        if choice == "q":
            break
        if choice in MENU:
            print()
            try:
                MENU[choice][1]()
            except Exception as e:
                print(f"Error while running this exercise: {e}")
        else:
            print("Invalid choice.")