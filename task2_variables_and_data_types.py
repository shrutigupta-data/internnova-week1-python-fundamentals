integer_value = 25
float_value = 3.14
string_value = "Python"
boolean_value = True

values = [
    ("Integer", integer_value),
    ("Float", float_value),
    ("String", string_value),
    ("Boolean", boolean_value),
]

for label, value in values:
    print(f"{label}: {value} | Type: {type(value).__name__}")
