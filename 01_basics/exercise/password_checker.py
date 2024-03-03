user_name = input("What's your name?\n")
password = input("What's your password you like?\n")

pwd_len = len(password)
hidden_pwd = '*' * pwd_len

# 在 f-string 中， {} 是占位符，可以放任何表达式，包括函数调用
print(f'Hi {user_name}, your password {hidden_pwd} is {pwd_len} characters long.')