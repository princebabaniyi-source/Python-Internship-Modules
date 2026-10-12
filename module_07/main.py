# File Handling

with open("sample.txt", "w") as file:
    file.write("This is my first Python file.\n")

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
