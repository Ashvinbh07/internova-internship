# 1. String Operations
text = "Hello, World!"
print("String Operations")

print("Original String:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Replace:", text.replace("World", "Duniya"))
print("Find 'World':", text.find("World"))

# 2. List Operations
fruits = ["apple", "banana", "cherry"]
print("\nList Operations")

print("Original List:", fruits)

fruits.append("mango")
print("After Append:", fruits)

fruits.remove("banana")
print("After Remove:", fruits)

fruits.sort()
print("After Sort:", fruits)

# 3. Tuple Creation and Indexing
student = ("Ashvin", 22, "Computer Engineering")
print("\nTuple Operations")

print("Student Tuple:", student)
print("Student Name:", student[0])
print("Student Age:", student[1])
print("Student Branch:", student[2])

# 4. Dictionary Operations
print("\nDictionary Operations")

student_info = {
    "name": "Ashvin",
    "college": "Thapar University",
    "branch": "Computer Engineering",
    "year": 2026
}

print("\nStudent Information:", student_info)
print("Student Name:", student_info["name"])
print("College:", student_info["college"])
print("Branch:", student_info["branch"])
print("Year:", student_info["year"])

# 5. Set Operations
print("\nSet Operations")

numbers = {10, 20, 30, 40}
print("Original Set:", numbers)

numbers.add(50)
print("After add:", numbers)

numbers.remove(20)
print("After remove:", numbers)