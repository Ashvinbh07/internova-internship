# input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# operations
sum = num1 + num2
difference = num1 - num2
product = num1 * num2

# results
print(f"Sum: {sum}")
print(f"Difference: {difference}")
print(f"Product: {product}")

# division and modulus
if num2 != 0:
    division = num1 / num2
    modulus = num1 % num2
    print(f"Division: {division}")
    print(f"Modulus: {modulus}")
else:
    print("Division and modulus by zero are not allowed.")
