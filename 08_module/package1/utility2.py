def greeting():
    print("Hello, I am utility2")


'''
在Python中，__name__是一个内置的特殊变量。当一个Python文件被直接运行时，__name__的值会被设置为__main__。
如果该文件被导入为模块，__name__的值则会被设置为该模块的名字。

例如， 如果你有一个名为main.py的文件，当你直接运行这个文件（例如，通过命令python main.py）时，__name__的值会是__main__。
但是，如果你在另一个Python文件中导入main.py（例如，通过import main），那么main.py中的__name__的值就会是main。
这个特性常常被用来在文件被导入时阻止某些代码的执行，或者改变程序的行为。例如，你可能会看到这样的代码：
'''
if __name__ == "__main__":
    print("utility2 is being run directly")
