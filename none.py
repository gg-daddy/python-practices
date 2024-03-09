# 可以通过globals()和locals()函数来查看全局和局部变量
x =1
print(globals())

def func():
    y = 1
    print(locals())    
    
func() 
print(globals())

# 通过 is None 和 is not None 来判断一个变量是否为None
test = None
print(test is None)
print(test is not None)


# is 用来判断两个变量引用对象是否为同一个， == 用来判断引用变量的值是否相等
a = [1, 2, 3]
b = a
print(a is b)  # Output: True

c = [1, 2, 3]
print(a is c)  # Output: False
print(a == c)  # Output: False