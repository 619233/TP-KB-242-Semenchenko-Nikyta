student = [
    "Aaron",
    "Benjamin",
    "Charles",
    "Daniel",
    "Edward",
    "Frank",
    "George",
    "Henry",
    "Isaac",
    "Jack",
    "Kevin",
    "Liam",
    "Michael",
    "Nathan",
    "Oliver",
    "Paul",
    "Quentin",
    "Robert",
    "Samuel",
    "Thomas",
    "Ulysses",
    "Victor",
    "William",
    "Xavier",
    "Yusuf",
    "Zachary"
]

import bisect

def insert(student):
    name = input("Встав нове ім'я в БД: ")
    bisect.insort(student, name)
    print("\n Updated list:")
    for student in student:
        print(student)
insert(student)