
class PlayerCharacter:

    MEMBER_SHIP = True  # class object attribute

    def __init__(self, name, age=0):
        if age > 18:
            self.name = name
            self.age = age
        else:
            raise ValueError('You are not allowed to play the game')

    def run(self):
        print('run')

    def __str__(self):
        return f"""name: {self.name}, age: {self.age}"""

    def __repr__(self):
        return f'PlayerCharacter("{self.name}", {self.age})'

    '''
    classmethod 和 staticmethod 提供了一种将方法与类关联，而不是与实例关联的方式。    
    '''
    # 类方法， 第一个参数必须是 cls，代表类本身。
    @classmethod  # decorator
    def adding_ages(cls, num1, num2):
        print(cls)
        # 可以通过 cls()， 来调用 __init__， 创建新的实例对象。
        return cls('Teddy from cls', num1 + num2)

    # 静态方法，不需要 cls 参数。也就意味着，静态方法中不能访问类变量。
    @staticmethod
    def static_method():
        print('static method')


player1 = PlayerCharacter('Andy', 20)
player2 = PlayerCharacter('Tom', 20)
print(hex(id(player1)))
# <__main__.PlayerCharacter object at 0x7f8e3e3e3f10>  # 0x7f8e3e3e3f10 是 player1 对象的内存地址， 和上面的 hex(id(player1)) 是一样的。
# 每次调用，地址都会变化，因为每次调用都会创建一个新的对象。
print(player1)
print(player2)

# <bound method PlayerCharacter.run of <__main__.PlayerCharacter object at 0x104b910a0>>
# 绑定方法是一种特殊的方法，它将方法的第一个参数（通常是 self）绑定到实例对象上。
print(player1.run)

print(repr(player1))
print(id(player1))
player3 = eval(repr(player1))  # 通过 eval 函数，可以将字符串转换为代码。
print(id(player3))

player1.MEMBER_SHIP = False  # 会创建一个新的实例变量，而不是修改类变量。
print(player1.MEMBER_SHIP)
print(player2.MEMBER_SHIP)
print(PlayerCharacter.MEMBER_SHIP)  # 可以通过类名访问类变量，也可以通过实例名访问类变量。
PlayerCharacter.MEMBER_SHIP = False  # 类变量是共享的，修改类变量会影响所有的实例变量。
print(PlayerCharacter.MEMBER_SHIP)
print(player2.MEMBER_SHIP)

player4 = PlayerCharacter.adding_ages(2, 18)
print(player4)

PlayerCharacter.static_method()
