
import inspect

print(inspect.getmro(ZeroDivisionError))
print(inspect.getmro(KeyboardInterrupt))

'''
Python的错误体系基于异常对象，所有的错误都是从BaseException类派生出来的。这个类的直接子类包括SystemExit，KeyboardInterrupt和Exception等。
Exception类是几乎所有的编程错误的基类，它的子类包括IOError，ValueError，ZeroDivisionError，TypeError，IndexError，KeyError等等。
'''
