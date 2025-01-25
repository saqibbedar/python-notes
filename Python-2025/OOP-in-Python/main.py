from Student import Student, GraduateStudent

students = [
    Student(1, "Alice Johnson", 2025, {"History": 75, "Math": 85}),
    Student(2, "Bob Smith", 2026, {"Science": 90, "English": 70}),
    GraduateStudent(3, "Charlie Brown", 2024, {"Physics": 88, "Chemistry": 92}, "Quantum Computing"),
    GraduateStudent(4, "Diana Prince", 2023, {"Biology": 95, "Math": 89}, "Genetic Engineering")
]

for student in students:
    student.display()
    print("-------------------------------------------------")

