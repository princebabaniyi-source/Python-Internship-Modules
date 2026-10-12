# Dictionaries

student = {
    "name": "Emma",
    "age": 21,
    "course": "Data Science"
}

print(student)
print(student["name"])

student["age"] = 22
print(student)

for key, value in student.items():
    print(key, value)
