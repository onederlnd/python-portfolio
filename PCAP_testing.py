import os
import random
import time

def load_questions(filename):
    """Load questions from a text file."""
    if not os.path.exists(filename):
        print(f"File '{filename}' not found.")
        return []

    questions = []
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read().split("\n\n")
        for block in content:
            lines = block.strip().split("\n")
            if len(lines) < 3:
                continue
            prompt = lines[0]
            options = lines[1:-1]
            answer = lines[-1].strip().upper()
            questions.append({
                "prompt": prompt,
                "options": options,
                "answer": answer
            })
    return questions

def run_exam(questions):
    """Run a full PCAP-style exam simulation."""
    random.shuffle(questions)
    user_answers = []

    print("\n=== PCAP Exam Simulator ===")
    print(f"Total questions: {len(questions)}")
    print("Answer each question with A, B, C, or D.\n")
    input("Press Enter to start the exam...")

    start_time = time.time()

    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}/{len(questions)}:")
        print(q["prompt"])
        for opt in q["options"]:
            print(opt)

        while True:
            ans = input("Your answer (A/B/C/D): ").strip().upper()
            if ans in ["A", "B", "C", "D"]:
                break
            print("Please enter a valid choice: A, B, C, or D.")

        user_answers.append(ans)

    end_time = time.time()
    duration = int(end_time - start_time)

    # Compute score
    score = 0
    for q, ans in zip(questions, user_answers):
        if ans == q["answer"]:
            score += 1

    print("\n=== Exam Finished ===")
    print(f"Your score: {score}/{len(questions)}")
    print(f"Time taken: {duration // 60} min {duration % 60} sec")

if __name__ == "__main__":
    filename = input("Enter question file path: ").strip()
    questions = load_questions(filename)
    if questions:
        run_exam(questions)
