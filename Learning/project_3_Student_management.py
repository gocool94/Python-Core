# ============================================
# Student Result & Attendance Management System
# Using List, Tuple, Set & Dictionary
# ============================================

print("\n🎓 STUDENT MANAGEMENT SYSTEM 🎓")
print("----------------------------------")

# --------------------------------------------
# 1. Subjects (TUPLE - Fixed)
# --------------------------------------------
subjects = ("Maths", "Science", "English")

# --------------------------------------------
# 2. Students List (LIST)
# --------------------------------------------
students = []

# --------------------------------------------
# 3. Attendance (SET)
# --------------------------------------------
present_students = set()

# --------------------------------------------
# 4. Marks Storage (DICTIONARY)
# --------------------------------------------
marks = {}

# --------------------------------------------
# 5. Number of Students
# --------------------------------------------
count = int(input("\nEnter number of students: "))

# --------------------------------------------
# 6. Student Data Entry
# --------------------------------------------
for i in range(count):
    print(f"\nEnter details for Student {i+1}")
    name = input("Student Name: ").title()
    students.append(name)

    # Attendance Input
    attendance = input("Is student present? (yes/no): ").lower()
    if attendance == "yes":
        present_students.add(name)

    # Marks Input
    marks[name] = {}
    for subject in subjects:
        score = int(input(f"Enter {subject} marks: "))
        marks[name][subject] = score

# --------------------------------------------
# 7. Final Report Generation
# --------------------------------------------
print("\n📋 FINAL STUDENT REPORT")
print("----------------------------------")

for student in students:

    print("\nStudent Name:", student)

    # Attendance Check
    if student in present_students:
        print("Attendance: Present")
    else:
        print("Attendance: Absent")

    # Marks Calculation
    student_marks = marks.get(student)
    total = sum(student_marks.values())
    average = total / len(subjects)

    # Grade Logic
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "Fail"

    print("Marks:", student_marks)
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)
    print("----------------------------------")

print("\n✅ Report Generated Successfully!")
