

while True:
    try:
        age = int(input("Enter your age: "))
        10 / age
    except ValueError as err:
        # err 为 ValueError 的错误信息
        print('*' * 40)
        print(type(err))
        print(dir(err))
        print('*' * 40)
        print(f"Please enter a number.\n Original Error: {err}")
    except ZeroDivisionError:
        print("Please enter age higher than 0")
    except (KeyboardInterrupt, TypeError) as err:  # 可以捕获多个错误
        print(f"Please enter a number.\n Original Error: {err}")
    except:  # 捕获所有错误
        print("Unknown error")
    else:
        print("You are", age, "years old")  # else 部分可以访问到 try 部分的变量
        break
    finally:
        # 无论是否有异常， 无论前面是否有 break/continue， finally 部分都会被执行。
        print("Finally block is always executed")

    print("Can you hear me?")  # 这段代码是否被执行，取决于是否有 break/continue。
