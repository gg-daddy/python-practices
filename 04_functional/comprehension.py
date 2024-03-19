
# 利用 comprehension 查找重复的元素

some_list = [1, 2, 3, 4, 5, 6, 7, 8, 4, 6]
duplicates = list({x for x in some_list if some_list.count(x) > 1})
print(duplicates)
