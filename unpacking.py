t = (1, 2, 3)
a, b, c = t
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

s = "abc"
a, b, c = s
print(a)  # Output: 'a'
print(b)  # Output: 'b'
print(c)  # Output: 'c'

d = {'name': 'John', 'age': 30}
print(d.values())
name, age = d.values()
print(name)  # Output: 'John'
print(age)  # Output: 30

def func(a, b, c, *args, ** kwargs):
    print(a, b, c)

args = [1, 2, 3,4 ]
func(*args)  # Output: 1 2 3

kwargs = {'a': 4, 'c': 6 ,'b': 5 }
func(**kwargs)  # Output: 4 5 6

kwargs = {'a': 4, 'c': 6 ,'b': 5, 'd': 7}
func(**kwargs) 