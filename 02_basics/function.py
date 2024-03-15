'''
positional 和 keyword 是针对函数调用者而言的, 而不是函数定义者.
'''


def display(name, age=30, *args, **kwargs):
    print(f"Name: {name}, Age: {age}")
    for arg in args:
        print(arg)
    print("-" * 40)
    for k, v in kwargs.items():
        print(f"{k}: {v}")


# default arguments
display("John")

# positional arguments
display("John", "a", "test1", "test2")

# keyword arguments
display(age=100, name="John", test1=123, test2=345)

print("*" * 40)

kwargs = {
    "name": "Eason",
    "age": 9,
    "test1": 123,
    "test2": 345,
    "test3": 567
}

display(**kwargs)

print("*" * 40)

args = list(("Ema", 4, "test1", "test2"))
display(*args)

# display(*args, **kwargs)  # got multiple values for argument 'name'
