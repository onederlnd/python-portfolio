# Practice OOP - Student Score Tracker

A command-line gradebook for tracking student scores for PCAP practice.  
This tool collects student names and scores, calculates averages, identifies top performers, tracks passing students, and saves/loads data to/from a file.

---

## Features

- add or update student names and scores via CLI  
- view all students and their scores  
- calculate class average  
- identify highest score and top student(s)  
- track students who passed (score >= 70)  
- save and load data from `gradebook.txt`  

---

## Getting Started

### Requirements

- python 3.8 or higher  
- works on windows, mac, and linux

### Installation

1. clone the repository:

git clone https://github.com/onederlnd/python-portfolio.git

2. navigate into the project folder:

cd student-score-tracker

3. run the main program:

python main.py

---

## Usage

When you run the program:

- you will be prompted to **enter a student name**  
- enter the **student score** as an integer  
- type `q` at the name prompt to quit and process data  

The program will:

- display all student names and scores  
- calculate and display the **class average**  
- show the **highest score** and the student(s) who achieved it  
- list all **passing students** (score >= 70)  
- save all entries to `gradebook.txt`  

---

## File Structure

practice-oop/  
├─ main.py           # main program loop and data processing  
├─ gradebook.txt     # saved student data (created automatically)  

---

## Example

Input:  
- Alice → 85  
- Bob → 92  
- Charlie → 68  

Output:  
- Alice: 85  
- Bob: 92  
- Charlie: 68  
- Average score: 81.67  
- Highest score: 92 by Bob  
- Passing students: Alice, Bob  

---

## Contributing

This project is self-contained for practice, but contributions are welcome:

- add support for multiple attempts per student  
- allow editing/deleting student scores  
- improve CLI with menu and color output  
- add additional statistics (median, standard deviation)  

---

## License

MIT License