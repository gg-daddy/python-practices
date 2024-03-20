import random
import sys


def random_answer(start, end):
    try:
        i_start = int(start)
    except ValueError:
        return "Start number must be an integer!"
    try:
        i_end = int(end)
    except ValueError:
        return "End number must be an integer!"
    return random.randint(i_start, i_end)


def guess_answer(answer, guess):
    return answer == guess


if __name__ == "__main__":
    random_num = random_answer(sys.argv[1], sys.argv[2])
    while True:
        try:
            guess = int(input(f"Guess the number:"))
            if guess_answer(random_num, guess):
                print("You got it!")
                break
        except ValueError:
            print("Guess number must be an integer")
            continue
