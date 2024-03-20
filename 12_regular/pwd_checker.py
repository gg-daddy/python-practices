import re

regex = r"[a-zA-Z0-9@#$%^&*]{8,}\d"
pattern = re.compile(regex)

match = pattern.fullmatch("Python@13fasdfasf1")  # None
if match:
    print(match)
