pictures = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1]
]


def display_picture(picture, fill_char='*', empty_char=' '):
    for row in picture:
        for pixel in row:
            print(fill_char if pixel else empty_char, end='')
        print()


display_picture(pictures, fill_char='@', empty_char="")
