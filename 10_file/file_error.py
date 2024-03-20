try:
    # 尝试打开文件
    with open("../.gitignore", "r") as file:
        1 / 0  # 异常的处理顺序，参见： ../11_context_manager/context_manager_class.py
except FileNotFoundError:
    # 如果文件不存在，捕获FileNotFoundError异常
    print("The file does not exist.")
except PermissionError:
    # 如果没有适当的权限，捕获PermissionError异常
    print("You do not have permission to access this file.")
except Exception as e:
    # 如果有其他类型的异常，捕获它
    print(f"An error occurred: {str(e)}")
