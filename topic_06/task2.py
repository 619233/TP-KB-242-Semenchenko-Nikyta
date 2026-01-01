students = [
    {"name": "Ivan", "mark": 85},
    {"name": "Petro", "mark": 60},
    {"name": "Anna", "mark": 95},
    {"name": "Oleg", "mark": 70}
]

for student in sorted(students, key=lambda student: student['mark']):
    print(f"Your name is {student['name']} your mark is {student['mark']}")