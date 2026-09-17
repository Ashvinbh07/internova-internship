# Program 1: Print numbers from 1 to 20 using for loop
print("Numbers from 1 to 20:")

for number in range(1, 21):
    print(number, end=" ")

print("\n")

# Program 2: Multiplication table
num = int(input("Enter a number for multiplication table: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Program 3: Print even numbers from 1 to 50 using while loop
print("\nEven numbers from 1 to 50:")

num = 2

while num <= 50:
    print(num, end=" ")
    num += 2
    