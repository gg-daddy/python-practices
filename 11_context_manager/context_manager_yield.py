import time
from contextlib import contextmanager


@contextmanager
def timer():
    """
    在这个例子中，timer函数是一个生成器。当你进入with语句块时，生成器会运行到yield语句，开始计时。
    当你离开with语句块时，生成器会从yield语句处继续运行，结束计时并打印出消耗的时间。
    这种方法的优点是更简洁，不需要定义一个完整的类。
    但是，它只适用于简单的上下文管理器，如果你需要在__exit__方法中处理异常，或者在__enter__方法中返回一个值，那么你仍然需要定义一个类。
    """
    start = time.time()
    yield "hello"
    end = time.time()
    print(f"Elapsed time: {end - start} seconds")


with timer() as value:
    # Your code here
    print(value)
    pass


@contextmanager
def open_file(file, mode="r"):
    file = open(file, mode)  # 创建资源
    try:
        yield file  # yield 语句的返回值是 resource
    finally:
        file.close()  # 清理资源


with open_file("../.gitignore") as res:
    print(res.read())
