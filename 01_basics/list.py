
cart = ["Toys", "Books", "Pens", "Pencils", "Notebooks"]
new_cart = cart[:] # 复制一个新的数组
new_cart[0] = "Gum"
print(cart)
print(new_cart)

new_cart2 = cart # 两个变量指向同一个数组
new_cart2[0] = "Wine"
print(cart)
print(new_cart)
print(new_cart2)

mixup_types = [1,2.0, "wood", True] # Python 的数组是可以混合类型的
print(mixup_types)

# delete index 2
del mixup_types[2] # 删除指定位置的元素

# remote last element
mixup_types.pop() # 删除最后一个元素
mixup_types.pop(0) # 也可以通过 pop 指定 index 进行删除
print(mixup_types)
mixup_types.remove(2) # 只删除第一个匹配值的元素
print(mixup_types)

# 创建一个包含重复元素的列表
my_list = [1, 2, 3, 2, 3, 4, 3, 4, 4]

# 删除所有值为 3 的元素
my_list = [x for x in my_list if x != 3] #列表推导式
print(my_list)  # 输出：[1, 2, 2, 4, 4, 4]