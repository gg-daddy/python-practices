
d = {}
d[1] = 1234
d['1'] = 1
d[False] = 1
d[0] = 12
print(d)
del d[1]   
print(d)

for key in d:
    print(key, d[key])

for key in d.keys():
    print(key, d[key])
    
for item in d.items():
    print(type(item))
    print(item)

d = {'name': 'John', 'age': 30}

dv = d.values() #dict_values， 是动态视图，会随着原字典的变化而变化。 类似的， items()和 keys() 也是动态视图。
dk = d.keys()
di = d.items()
for value in dv:
    print(value)

d["birth"] = 1930
print(dv)
print(dk)
print(di)

d2 = d.copy() 
print(d2)
d['test'] = "test001"
print(d2)
print(d)

d.clear()
print(d2)

name = d2.get('name')
print(name)

t = d2.get("test", "default-test")
print(t)

# 从 python 3.7 开始，字典是有序的。在之前的版本中，字典是无序的。popitem 会删除最后添加的元素
poped = d2.popitem()
print(d2)
print(poped)

name_value = d2.pop("name")
print(d2)
print(name_value)

print('---------')
print(d2)
# upinsert 操作.
d2.update({'name': 'John', 'age': 33})
print(d2)

# dict 的 key 必须是 immutable 的，所以 list 是不能作为 key 的。但是 tuple 可以作为 key
d3 = {
    (1,2) : "Tuple Value"    
}
print(d3[(1,2)])