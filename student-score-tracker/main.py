# practice-oop student score tracker
# a command-line gradebook for tracking student scores for pcap practice

import os

filename = "gradebook.txt"

# --- load students from file
def load_students():
    """load students and scores from gradebook file"""
    students = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    student_name, student_score = line.split(",")
                    students[student_name] = int(student_score)
        print("Load successful")
    except FileNotFoundError:
        print("[ERROR] File not found, starting with empty gradebook")
    except Exception as e:
        print(f"[ERROR] Could not load students from file: {e}")
    return students

# --- save students to file
def save_students(students):
    """save students and scores to gradebook file"""
    try:
        with open(filename, "w") as f:
            for name, score in students.items():
                f.write(f"{name},{score}\n")
        print("Save successful")
    except Exception as e:
        print(f"[ERROR] Could not save students: {e}")

# --- add or update student
def add_student(students):
    """add a student and score"""
    student_name = input("Enter student name (or 'q' to quit): ").strip()
    if student_name.lower() == "q":
        return False
    try:
        student_score = int(input(f"Enter score for {student_name}: "))
        students[student_name] = student_score
    except ValueError:
        print("[ERROR] Please enter a valid number")
    return True

# --- calculate statistics
def calculate_stats(students):
    """calculate average, highest score, and passing students"""
    if not students:
        return None, None, []
    
    avg_score = sum(students.values()) / len(students)
    highest_score = max(students.values())
    top_students = [name for name, score in students.items() if score == highest_score]
    passing_students = [name for name, score in students.items() if score >= 70]
    
    return avg_score, highest_score, top_students, passing_students

# --- display results
def display_results(students):
    """display student scores and statistics"""
    avg_score, highest_score, top_students, passing_students = calculate_stats(students)
    
    if not students:
        print("No students in gradebook")
        return

    print("\n--- student scores ---")
    for name, score in students.items():
        print(f"{name}: {score}")
    
    print(f"\nAverage score: {avg_score:.2f}")
    print(f"Highest score: {highest_score} by {', '.join(top_students)}")
    print(f"Passing students: {', '.join(passing_students)}\n")

# --- main program loop
def main():
    students = load_students()
    
    while True:
        if not add_student(students):
            break

    display_results(students)
    save_students(students)

# --- run program
if __name__ == "__main__":
    main()