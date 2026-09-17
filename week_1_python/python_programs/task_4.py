# input marks
marks = float(input("Enter your marks (0-100): "))

# Checking marks and displaying the grade
if marks < 0 or marks > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")

elif marks >= 90:
    print("Grade: A")

elif marks >= 75:
    print("Grade: B")

elif marks >= 60:
    print("Grade: C")

else:
    print("Grade: Fail")