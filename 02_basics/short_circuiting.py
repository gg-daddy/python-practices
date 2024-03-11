

def is_friend():
    print("checking if friend...")
    return True


def is_valid():
    print("checking if valid...")
    return False


if is_friend() and is_valid():
    print("short circuiting for 'and'.")

print("============")

if is_friend() or is_valid():
    print("short circuiting for 'or'.")
