
birth = input("Which year were you born?")
try:
    birth_year = int(birth.strip())
except ValueError:
    print("Invalid input. Please enter a valid year.")
    exit(1)

from datetime import datetime
current_year = datetime.now().year
age = current_year - birth_year
print(f"You are {age} years old")