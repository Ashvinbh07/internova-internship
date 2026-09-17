name = "Ashvin Bhatt"
college = "Thapar University"
branch = "Computer Engineering"

introduction = (
    f"Hello, my name is {name}.\n"
    f"I study at {college}.\n"
    f"My branch is {branch}.\n"
    "I am learning Python for Data Analytics."
)

file_path = "introduction.txt"

with open(file_path, "w") as file:
    file.write(introduction)

with open(file_path, "r") as file:
    content = file.read()

print(content)