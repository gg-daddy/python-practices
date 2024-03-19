
func_keep = {}


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Now, wrap the function: {func.__name__}")
        func_keep.update({func.__name__ + "_keep": func})
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper


@my_decorator
def hello(name):
    print(f"To: {name}: \nHello, world!")


print(hello)
print(hello.__name__)
print(type(hello))

hello("John")
print(func_keep)
