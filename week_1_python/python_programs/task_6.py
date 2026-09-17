def calculate_square(number):
    return number * number

def calculate_average(num1, num2, num3):
    return (num1 + num2 + num3) / 3

# input from user
number = float(input("Enter a number to calculate its square: "))

num1 = float(input("Enter the first number for average: "))
num2 = float(input("Enter the second number for average: "))
num3 = float(input("Enter the third number for average: "))

square = calculate_square(number)
average = calculate_average(num1, num2, num3)

print(f"The square of {number} is: {square}")
print(f"The average of {num1}, {num2}, and {num3} is: {average}")