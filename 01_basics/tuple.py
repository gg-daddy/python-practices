
t = (1,2,3,10, 'a', 'b', 'c')
print(t)

#tuple 是 immutable 的，所以不能修改元素
# t[1] = 10 #'tuple' object does not support item assignment

a,b, *c = t
print(c) # 解包之后，c 是一个列表，包含了剩下的元素

print(t.count(1)) # 统计元素出现的次数
print(t.index(10)) # 返回元素的索引