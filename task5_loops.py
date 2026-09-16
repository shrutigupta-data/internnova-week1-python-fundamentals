print("Numbers from 1 to 20:")
for number in range(1, 21):
    print(number, end=" ")
print()

number = int(input("Enter a number for its multiplication table: "))
print(f"\nMultiplication table of {number}:")
for multiplier in range(1, 11):
    print(f"{number} x {multiplier} = {number * multiplier}")

print("\nEven numbers from 1 to 50:")
even_number = 2
while even_number <= 50:
    print(even_number, end=" ")
    even_number += 2
print()
