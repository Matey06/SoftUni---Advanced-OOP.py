number_of_students = int(input())

students_grades = {}

for _ in range(number_of_students):
    student, grade = input().split()
    if student not in students_grades:
        students_grades[student] = []
    students_grades[student].append(float(grade))

for key, values in students_grades.items():
    avr = sum(values) / len(values)
    print(f"{key} -> {' '.join([f'{el:.2f}' for el in values])} (avg: {avr:.2f})")
