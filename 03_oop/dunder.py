'''
dunder methods. 
'''


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.dict = {
            "name": name,
            "age": age
        }

    def attack(self):
        print(f'{self.name} is doing nothing.')

    def __str__(self):
        return f'name: {self.name}'

    def __len__(self):
        return 5

    def __del__(self):
        print('deleted')

    def __getitem__(self, item):
        return self.dict[item]


user1 = User("Bob", 40)
print(user1)  # 通过 __str__ 方法，可以通过 print() 函数获取实例的字符串表示。
print(str(user1))

print(len(user1))  # 通过 __len__ 方法，可以通过 len() 函数获取实例的长度。
print(user1["name"])  # 通过 __getitem__ 方法，可以通过索引的方式访问实例变量。

del user1  # this will call __del__ method.
