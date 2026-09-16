def square(number):
    return number * number


def average(first_number, second_number, third_number):
    return (first_number + second_number + third_number) / 3


number = float(input("Enter a number to square: "))
print(f"Square: {square(number)}")

numbers = [
    float(input("Enter the first number for the average: ")),
    float(input("Enter the second number for the average: ")),
    float(input("Enter the third number for the average: ")),
]
print(f"Average: {average(*numbers)}")
