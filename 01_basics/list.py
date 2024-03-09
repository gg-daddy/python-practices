
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


matrix = [
    [1,2,3,],
    [3,4,5],
    [6,7,8]
]

print(matrix[0][::-1])


mixup_types = [1,2.0, "wood", True]
print(mixup_types[2])

for x in mixup_types[2]:
    print(x)
    
g = (x + 'b' for x in mixup_types[2])

for x in g:
    print(x)
    
    
# add: append, extend, insert

basket = [1,2,3,4,5]

basket.append(100)
print(basket)

basket.insert(2, 200)
print(basket)

basket.extend([101,102,100])
print(basket)

# remove: pop, remove, del

basket.remove(100)
print(basket)

basket.pop()
print(basket)

basket.pop(0)
print(basket)

del basket[0]
print(basket)

# update: list[index] = new_value
# search: index, in operator

# basket.index(1000) # 如果不存在，会有 ValueError。 可以使用 in 操作符进行判断
is_exist = 1000 in basket
print(is_exist)

print(basket.count(3)) # 统计元素出现的次数

basket = [5,31,1,100]
basket.sort() # in-place sort
print(basket)

basket2 = sorted(basket) # 返回一个新的数组
print(basket2)
print(basket == basket2)

basket.reverse() # in-place reverse
print(basket) # 先 sort， 再 reverse，就是逆序.


basket_copy = basket.copy() # 复制一个新的数组
basket_copy2 = list(basket) # 复制一个新的数组
basket_copy3 = basket[:] # 复制一个新的数组

basket_reverse = basket[::-1] # 复制一个新的数组，并且逆序 ， 相比 reverse 不是 in-place 的。

r = range(1,100)
print(r)
print(list(r))

string_list = ["How","are","you","doing","?"]
print(' '.join(string_list))

# list unpacking
p = [1,2,3,4,5,6,7,8,]
#* 符号用于收集剩余的值
a,b,*c,d = p 
print(a)
print(b)
print(c)
print(d)

a,b,*_ = p 
print(a)
print(b)
print(_)
