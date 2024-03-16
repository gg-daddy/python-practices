
some_list = [1, 2, 3, 4, 5]

# 写法1
if len(some_list) > 1:
    print(f"list lenth is {len(some_list)}")

# 写法2
length = len(some_list)
if length > 1:
    print(f"list lenth is {length}")

# 写法 3. warlus opeartor (海象运算符)
# 这个运算符允许你在表达式中赋值，并立即使用这个值。
if (n := len(some_list)) > 1:
    print(f"list lenth is {n}")
