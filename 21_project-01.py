 # Data
students = [
    ("Rukunuddin", "Physics", 88.456),
    ("Rukunuddin", "Python", 95.0),
    ("Rukunuddin", "Math", 91.25),
    ("Rukunuddin", "English", 84.75)
]

# Header
print("{:<12} | {:<10} | {:>7}".format("Student", "Subject", "Marks"))
print("-" * 35)

# Rows
for name, subject, marks in students:
    print("{:<12} | {:<10} | {:>7.2f}".format(name, subject, marks))

# Average
average = sum(marks for _, _, marks in students) / len(students)
print("-" * 35)
print("{:<12} | {:<10} | {:>7.2f}".format("Average", "", average))