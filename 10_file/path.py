from pathlib import Path

# Create a Path object for the directory
dir_path = Path("../")

# Iterate over all files and directories in the directory
for item in dir_path.iterdir():
    # Check if the item is a file
    if item.is_file():
        print(f"File: {item}")
    # Check if the item is a directory
    elif item.is_dir():
        print(f"Directory: {item}")

"""
在 pathlib 库中，Path 类是用来表示文件系统路径的。你可以使用 / 运算符来连接多个路径组件，创建一个新的 Path 对象。  
1.在你的例子中，Path('directory') / 'subdirectory' / 'file.txt'，这个表达式创建了一个新的 Path 对象，
    表示的路径是 'directory/subdirectory/file.txt'。  
2.这里的 / 运算符是 Path 类重载的，它的作用是连接路径。当你使用 / 运算符连接两个 Path 对象，或者一个 Path 对象和一个字符串时，
    它会返回一个新的 Path 对象，表示的是这两个路径组件连接后的路径。  

这种方式的好处是，你可以使用简洁的语法来构建路径，而不需要关心不同操作系统的路径分隔符差异。
Path 类会自动处理这些差异，确保你构建的路径在任何操作系统下都是有效的。
"""
p = Path("..") / "10_file" / "path.py"
print(p)
print(type(p))
