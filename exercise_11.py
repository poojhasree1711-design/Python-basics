#1
# Problem: Student Attendance Analyzer
# A class has attendance data for 30 days stored as a list (1 = present, 0 = absent).
# Tasks:
# Count total present days
# Count total absent days
# Calculate attendance percentage
# Print “Eligible” if attendance ≥ 75%, else “Not Eligible” give me code for this!

#Attendance list:-
attendance = [1, 1, 0, 1, 1, 0, 1, 1, 1, 0,1, 1, 1, 1, 0, 1, 0, 1, 1, 1,1, 0, 1, 1, 1, 1, 0, 1, 1, 1]

#Total days
total_days = len(attendance)

#Count present and absent
present_days = attendance.count(1)
absent_days = attendance.count(0)

#Calculate percentage
attendance_percentage=(present_days/total_days)*100

#Display results
print("Total Present Days:", present_days)
print("Total Absent Days:", absent_days)
print("Attendance Percentage:", attendance_percentage, "%")

#Eligibility check
if attendance_percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")

#2
# Problem: Student Performance Filter
# Given a dictionary:
# students = {
#"Arun": 85,
#"Bala": 45,
#"Charan": 72,
#"Divya": 90}
# Tasks:
# Create a new dictionary of students who scored ≥ 75
# Create a list of students who failed (< 50)
# Create a list of grades using comprehension

#Student performance:-
students = {
    "Arun": 85,
    "Bala": 45,
    "Charan": 72,
    "Divya": 90
}

#Students with marks>=75 using comprehension
top_students = {name: marks for name, marks in students.items() if marks >= 75}

#Students who failed marks<50 using comprehension
failed_students = [name for name, marks in students.items() if marks < 50]

#Grades list using comprehension
grades = ["A" if marks >= 75 else "B" if marks >= 60 else "C" if marks >= 50 else "F" for marks in students.values()]

print("Top Students:", top_students)
print("Failed Students:", failed_students)
print("Grades:", grades)