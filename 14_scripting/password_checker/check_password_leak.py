import hashlib
import sys

import requests


def get_pwned_count(query_pwd):
    """
    Function to check if the password has been leaked before and return back the count of times it has been leaked.
    """
    hashed_pwd = hashlib.sha1(query_pwd.encode("utf-8")).hexdigest().upper()
    first5_char, hashed_tail = hashed_pwd[:5], hashed_pwd[5:]
    response = requests.get("https://api.pwnedpasswords.com/range/" + first5_char)
    if response.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {response.status_code}, check the API and try again."
        )

    hashed_tail_pairs = (line.split(":") for line in response.text.splitlines())
    for hashed_back_tail, count in hashed_tail_pairs:
        if hashed_back_tail == hashed_tail:
            return int(count)
    return 0


def show_password_leak_info(pwd_list):
    for pwd in pwd_list:
        count = get_pwned_count(pwd)
        if count:
            print(f"\033[31m {pwd} was found {count} times.\033[0m")
        else:
            print(f"\033[32m {pwd} was not found. Your password is safe!\033[0m")


if __name__ == "__main__":
    pwd_list = sys.argv[1:]
    show_password_leak_info(pwd_list)
    sys.exit("All passwords checked!")
