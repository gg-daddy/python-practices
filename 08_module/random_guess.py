import random
import sys

try:
    start = int(sys.argv[1])
except ValueError:
    print("Start number must be an integer")
    sys.exit(1)
try:
    end = int(sys.argv[2])
except ValueError:
    print("End number must be an integer")
    sys.exit(1)

random_num = random.randint(start, end)

while True:
    try:
        guess = int(input(f"Guess the number: {start} ~ {end}"))
        if guess == random_num:
            print("You got it!")
            break
    except ValueError:
        print("Guess number must be an integer")
        continue
