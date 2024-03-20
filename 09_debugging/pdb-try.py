import pdb

"""
pdb 是 Python 的内置调试器，它可以让你在代码执行过程中进行交互，以便更好地理解代码的运行情况。
你可以使用 pdb 来设置断点、单步执行代码、查看变量值等。
你可以在代码中使用 import pdb; pdb.set_trace() 来设置断点。当 Python 解释器执行到这一行时，它会自动进入 pdb 调试模式。
"""


def add(a, b):
    pdb.set_trace()
    return a + b


print(add(1, 2))
