# Student Grade Analyzer Using Python

A beginner-friendly Python command-line application that analyzes student marks and generates an academic performance report.

## Features

- Accepts a student's name, subject names, and marks
- Validates marks from 0 to 100
- Calculates total and average marks
- Assigns a grade based on the average
- Determines PASS or FAIL (each subject must have at least 35 marks)
- Displays a formatted student report

## Concepts Used

Variables, data types, conditionals, loops, functions, lists/dictionaries (dictionary for subject marks), input validation, and basic calculations.

## Requirements

- Python 3.8 or newer
- No external libraries required

## Run the project

1. Clone this repository:
   ```bash
   git clone https://github.com/KageFlow/student-grade-analyzer.git
   ```
2. Open the project folder:
   ```bash
   cd student-grade-analyzer
   ```
3. Run:
   ```bash
   python main.py
   ```

On Windows, you can also use `py main.py`.

## Grade scale

| Average | Grade |
|---|---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| 35–49.99 | E |
| Below 35 | F |

**Pass rule:** A student passes only when every subject mark is at least 35.

## Example

```text
STUDENT GRADE ANALYZER
Enter student name: Alex
How many subjects? 3
Enter subject 1 name: Python
Enter marks for Python (0-100): 88
Enter subject 2 name: Maths
Enter marks for Maths (0-100): 76
Enter subject 3 name: DBMS
Enter marks for DBMS (0-100): 91

======================================
         STUDENT PERFORMANCE
======================================
Student: Alex
Python                 88.0
Maths                  76.0
DBMS                   91.0
--------------------------------------
Total marks:          255.0
Average:               85.00%
Grade:                     A
Result:                  PASS
======================================
```

## Project Structure

```
student-grade-analyzer/
├── main.py
├── README.md
└── .gitignore
```

## Internship Deliverables

- GitHub repository: https://github.com/KageFlow/student-grade-analyzer
- LinkedIn post: Share a short description of the project, what you learned, and the repository link.

## Author

KageFlow
