
'''
Python scope rules:
Python 的作用域规则可以归纳为 LEGB 规则，即：
1. Local（局部）：首先搜索的是包含变量的最内层函数或方法。如果在这个函数或方法中找到了变量，那么就使用这个变量。
2. Enclosing（封闭）：如果在局部作用域中没有找到变量，那么就搜索任何包含变量的封闭函数。封闭函数是指包含当前函数的外部函数。这个规则只适用于嵌套的函数。
3. Global（全局） ：如果在封闭作用域中没有找到变量，那么就搜索全局作用域。全局作用域是指包含所有代码的最外层。
4. Built-in（内置）：如果在全局作用域中没有找到变量，那么就搜索内置作用域。内置作用域是指包含 Python 的内置函数和变量的作用域。

Enclosing scope: 闭包作用域， 也叫封闭作用域，是指包含当前函数的外部函数。这个规则只适用于嵌套的函数。
Global scope: 全局作用域，是指包含所有代码的最外层。

'''
count = 5

# global 关键字


def increase_count():
    global count  # 使用 global 关键字，可以在函数内部修改全局变量的值. 但是不推荐使用 global 关键字，因为它会使代码变得难以理解。
    count += 1
    return count


increase_count()
increase_count()
print(count)

# nonlocal 关键字


def enclosing():
    count = 10

    def local():
        nonlocal count  # 使用 nonlocal 关键字，可以在函数内部修改封闭作用域中的变量的值。
        count += 1
        return count

    return local()


print(enclosing())
