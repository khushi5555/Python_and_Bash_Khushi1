students = {
    "Mahi": "A",
    "Simran": "B"
}

name = input("Enter student name: ")
grade = input("Enter student grade: ")


students[name] = grade

name = input("Enter student name to update: ")

if name in students:
    grade = input("Enter new grade: ")
    students[name] = grade

else:
    print("students not found")
    

print(students)