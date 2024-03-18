
class User:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print(f'{self.name} is doing nothing.')


class Wizard(User):

    def __init__(self, name, power):
        # super() 的主要优点之一是它提供了一种更加通用的方式来引用父类，而不需要显式地指定父类的名称。
        # 这使得代码更易于维护，因为如果你更改了类的继承关系，你不需要在每个使用了父类名称的地方进行修改。
        super().__init__(name)  # 使用 super() 和下面的效果是一样的，但是不用传递 self。
        # User.__init__(self, name)
        self.power = power

    def attack(self):
        print(f'{self.name} is casting a spell with power {self.power}.')


class Ancher(User):

    def __init__(self, name, arrows):
        super().__init__(name)
        self.arrows = arrows

    def attack(self):
        print(f'{self.name} is shooting arrows: {self.arrows}.')


wizard1 = Wizard('Merlin', 50)
archer1 = Ancher('Robin', 100)

for user in [wizard1, archer1]:
    user.attack()

print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))

print(dir(wizard1))

print(getattr(wizard1, 'name'))
m1 = getattr(wizard1, 'attack')
if callable(m1):
    m1()
