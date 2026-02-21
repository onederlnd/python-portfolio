# Practice OOP
# This is a student score tracker for PCAP practice.

"""collect data"""

filename = "gradebook.txt"


# --- load students from files
def load_students(filename):
    students = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                student_name, student_score = line.split(",")
                students[student_name] = int(student_score)
        print("Load successful")
    except FileNotFoundError:
        print("[ERROR] File not found, starting with empty gradebook")
    except Exception as e:
        print(f"[ERROR] Could not load students from file: {e}")
    return students


# save students to file
def save_students(filename, students):
    try:
        with open(filename, "a") as f:
            for name, score in students.items():
                f.write(f"{name},{score}\n")
        print("Write successful")
    except Exception as e:
        print(f"[ERROR] Could not write to file, {e}")


students = load_students(filename)

while True:
    student_name = str(input("Enter your name:"))
    if student_name == "q":
        break
    try:
        student_score = int(input("Enter your score:"))
        students[student_name] = student_score
    except ValueError:
        print("Please enter a valid number.")

save_students(filename, students)
""" process data """
# calculate average
avg_score = sum(students.values()) / len(students)

# calculate highest score
# highest_score =
highest_score = max(students.values())

for name, score in students.items():
    if score == highest_score:
        top_student = name
        break

# calculate passing students
# passing =
passing = []
for name, score in students.items():
    if score >= 70:
        passing.append(name)

""" display results """

# print all students and scores
for name, score in students.items():
    print(f"{name}: {score}")
# print average score
print("Average score:", avg_score)
# print highest score
print(f"Highest score: {highest_score} by {top_student}")
# print passing scores
print("Passing scores:", ", ".join(passing))
# print all students and their score first


#


save_students(filename, students)


load_students(filename)
