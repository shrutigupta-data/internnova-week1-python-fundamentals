text = "Python makes data analysis powerful"
print(f"Original string: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Replace: {text.replace('powerful', 'accessible')}")
print(f"Position of 'data': {text.find('data')}")

numbers = [30, 10, 20]
numbers.append(40)
numbers.remove(10)
numbers.sort()
print(f"\nList after append, remove, and sort: {numbers}")

student_tuple = ("Asha", "Computer Science", 21)
print(f"Tuple: {student_tuple}")
print(f"Tuple item at index 0: {student_tuple[0]}")

student = {"name": "Asha", "age": 21, "branch": "Computer Science"}
print(f"Student dictionary: {student}")

skills = {"Python", "SQL"}
skills.add("Excel")
skills.remove("SQL")
print(f"Set after add and remove: {skills}")