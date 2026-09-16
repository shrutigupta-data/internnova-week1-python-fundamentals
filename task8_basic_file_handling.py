file_name = "introduction.txt"
introduction = (
    "Hello, my name is Shruti. I am learning Python for Data Analytics.\n"
    "Python helps me work with data and solve problems."
)

with open(file_name, "w", encoding="utf-8") as file:
    file.write(introduction)

print(f"Created and wrote to {file_name}.")

with open(file_name, "r", encoding="utf-8") as file:
    contents = file.read()

print("\nFile contents:")
print(contents)