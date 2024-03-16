

def is_even(num: int):
    return num % 2 == 0


def highest_even(data: list[int]):
    return max((num for num in data if is_even(num)), default=None)


print(highest_even([10, 2, 3, 4, 5, 6, 7, 8, 9, 1]))
