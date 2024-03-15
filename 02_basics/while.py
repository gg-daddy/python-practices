

i = 0
while i < 50:
    print(i)
    i += 1
else:  # else 语句是可选的, 但是如果有的话, 它会在 while 循环结束后执行. 但是如果是通过 break 语句结束的, 那么 else 语句不会执行.
    print('Done!')

i = 0

while i < 50:
    if i >= 10:
        break

    print(i)
    i += 1
else:  # 上面的 while 是通过 break 语句结束的, 所以这里的 else 语句不会执行.
    print('Done!')

while True:
    resp = input('Enter something: ')
    if resp == 'quit':
        break
    print(resp)
