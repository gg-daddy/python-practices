
some_list = ['a', 'b', 'n', 'n']
counter = {}

for item in some_list:
    if item in counter:
        counter[item] += 1
    else:
        counter[item] = 1

for k, v in counter.items():
    if v > 1:
        print(f'{k} is duplicate')

duplicates = []
for item in some_list:
    if some_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)
print(duplicates)

duplicates.clear()
for i, v in enumerate(some_list):
    if v in some_list[i+1:] and v not in duplicates:
        duplicates.append(v)
print(duplicates)
