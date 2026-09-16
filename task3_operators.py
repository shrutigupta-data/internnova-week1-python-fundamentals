first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print(f"Addition: {first_number + second_number}")
print(f"Subtraction: {first_number - second_number}")
print(f"Multiplication: {first_number * second_number}")

if second_number == 0:
    print("Division: undefined (cannot divide by zero)")
    print("Modulus: undefined (cannot divide by zero)")
else:
    print(f"Division: {first_number / second_number}")
    print(f"Modulus: {first_number % second_number}")