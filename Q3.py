def get_integer(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid number. Please enter a number.")
def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"
def get_student_name():
    while True:
        name = input("Enter student name: ").strip()
        if name and not any(char.isdigit() for char in name):
            return name
        print("Invalid name. Please enter a name without numbers.")
num_students = get_integer("Enter number of students: ")
while num_students <= 0:
    print("Number of students must be greater than 0.")
    num_students = get_integer("Enter number of students: ")
students = {}
for i in range(num_students):
    print(f"\nStudent {i + 1}")
    name = get_student_name()
    score = get_integer("Enter student score (0-100): ")
    while score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        score = get_integer("Enter student score (0-100): ")
    students[name] = score
grade_count = {
    "A": 0,
    "B": 0,
    "C": 0,
    "F": 0
}
total_score = 0
retest_students = []
print("\n===== CLASS GRADE REPORT =====")
for name, score in students.items():
    grade = get_grade(score)
    print(f"{name} {score} {grade}")
    grade_count[grade] += 1
    total_score += score
    if score < 60:
        retest_students.append(name)
average = total_score / len(students)
top_name = max(students, key=students.get)
lowest_name = min(students, key=students.get)
print(f"\nAverage: {average:.2f}")
print(f"Top: {top_name} ({students[top_name]})")
print(f"Lowest: {lowest_name} ({students[lowest_name]})")
print(f"Grade count: {grade_count}")
if retest_students:
    print(f"Retest: {', '.join(retest_students)}")
else:
    print("Retest: None")