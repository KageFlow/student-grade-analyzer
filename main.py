"""Student Grade Analyzer - beginner-friendly command-line project."""

PASS_MARK = 35
MAX_MARK = 100


def get_mark(subject):
    """Read and validate a mark between 0 and 100."""
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (0-{MAX_MARK}): "))
            if 0 <= mark <= MAX_MARK:
                return mark
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def calculate_grade(average):
    """Return a grade based on the student's average."""
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    if average >= 35:
        return "E"
    return "F"


def analyze_student(name, marks):
    """Create a report dictionary from a student's marks."""
    total = sum(marks.values())
    average = total / len(marks) if marks else 0
    passed = all(mark >= PASS_MARK for mark in marks.values())

    return {
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": calculate_grade(average),
        "status": "PASS" if passed else "FAIL",
    }


def print_report(student):
    """Display a clear student performance report."""
    print("\n" + "=" * 38)
    print("         STUDENT PERFORMANCE")
    print("=" * 38)
    print(f"Student: {student['name']}")
    for subject, mark in student["marks"].items():
        print(f"{subject:<20} {mark:>6.1f}")
    print("-" * 38)
    print(f"{'Total marks:':<20} {student['total']:>6.1f}")
    print(f"{'Average:':<20} {student['average']:>6.2f}%")
    print(f"{'Grade:':<20} {student['grade']:>6}")
    print(f"{'Result:':<20} {student['status']:>6}")
    print("=" * 38)


def main():
    print("STUDENT GRADE ANALYZER")
    name = input("Enter student name: ").strip() or "Student"

    while True:
        try:
            count = int(input("How many subjects? "))
            if count > 0:
                break
            print("Enter at least one subject.")
        except ValueError:
            print("Please enter a whole number.")

    marks = {}
    for index in range(count):
        subject = input(f"Enter subject {index + 1} name: ").strip()
        subject = subject or f"Subject {index + 1}"
        marks[subject] = get_mark(subject)

    student = analyze_student(name, marks)
    print_report(student)


if __name__ == "__main__":
    main()
