'''
在编程中，制表符（Tab）和空格（Space）都是常用的缩进方法，但它们之间存在一些差异：
显示宽度：制表符的显示宽度可以在不同的编辑器或环境中进行设置，通常默认为8个空格的宽度，
但在许多现代编辑器中，可以设置为4个空格的宽度。而空格的显示宽度则是固定的，每个空格都占用一个字符的宽度。

存储空间：制表符只占用一个字符的存储空间，无论它在显示时占用多少宽度。而每个空格都占用一个字符的存储空间。
一致性：由于制表符的显示宽度可以变化，所以如果一个代码文件被在不同的编辑器或环境中打开，其排版可能会出现差异。而使用空格进行缩进则不会有这个问题，因为空格的显示宽度是固定的。
在 Python 中，官方的编程风格指南 PEP 8 建议使用4个空格进行缩进。这是为了保持代码的一致性和可读性。然而，无论选择使用制表符还是空格，最重要的是在一个项目中保持一致。
'''

is_valid = True

if is_valid:
    print("This is True")
else:
    print("This is False")
