import time


class Timer:
    """
    通过定义一个类并实现__enter__和__exit__方法来创建自定义的上下文管理器。
    __enter__方法在进入with语句块时被调用，而__exit__方法在离开with语句块时被调用。
    """

    def __enter__(self):
        print("Start timer")
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        这里的参数解释如下：
            exc_type：异常的类型。如果 with 语句块中没有发生异常，那么这个参数的值为 None。否则，它的值为发生的异常的类型。
            exc_val：异常的实例。如果 with 语句块中没有发生异常，那么这个参数的值为 None。否则，它的值为发生的异常的实例。
            exc_tb：一个追踪对象，它封装了异常的追踪信息。如果 with 语句块中没有发生异常，那么这个参数的值为 None。否则，它的值为一个追踪对象，封装了异常的追踪信息。
        __exit__ 方法可以返回一个布尔值。
            如果 __exit__ 返回 True，那么这个异常会被成功处理，程序会继续执行 with 语句块之后的代码。
            如果 __exit__ 返回 False 或者没有返回值（默认为返回 None），那么这个异常会被重新抛出，程序会停止执行 with 语句块之后的代码。
        """
        self.end = time.time()
        print(f"Elapsed time: {self.end - self.start} seconds")
        if exc_type is not None:
            print(f"Exception caught in __exit__: {exc_val}")
            print(type(exc_type))
            print(type(exc_val))
            print(type(exc_tb))
            return True  # 异常已经被处理，不会被抛出到外部


"""
expression通常是一个实现了上下文管理协议的对象，即它有__enter__和__exit__方法。
__enter__方法在进入with代码块之前被调用，而__exit__方法在离开with代码块时被调用。
在__exit__方法中，你可以处理异常，清理资源等。
下面的 Timer() 返回的 Timer 实例就是一个上下文管理器的例子。 
"""
try:
    with Timer() as timer:
        time.sleep(1)
        print("This is a test")
        1 / 0
        print("after exception")
except Exception as e:
    print(
        f"An error occurred: {str(e)}"
    )  # 这个异常会被Timer类的__exit__方法拦截处理，此处不会被执行。

print("End of the program")
