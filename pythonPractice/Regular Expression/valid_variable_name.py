import re


def is_valid_variable_name(variable_name):
    pattern = re.compile(r"[A-Za-z_][A-Za-z_0-9]*\Z")
    return bool(pattern.match(variable_name))


# Test cases
valid_names = ["_hidden", "L_value", "A123_"]
invalid_names = ["2abc", "$invalid", "spaces not allowed"]

print("Valid variable names:")
for name in valid_names:
    print(f"{name}: {is_valid_variable_name(name)}")

print("\nInvalid variable names:")
for name in invalid_names:
    print(f"{name}: {is_valid_variable_name(name)}")
