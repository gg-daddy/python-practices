# 字符串表示和拼接操作
a = 'hello'
b = "world"
print(a+' '+b)
long_sentence = '''
long string
exmaple
as
you 
see
'''
print(long_sentence)
print(type(long_sentence))

# type conversion
int_str = str(100)
print(type(int_str))
str_int = int('100')
print(type(str_int))
# print("123" + 5)

# escape sequence
print("hello\nworld")
print("It's a good day!")
print('It\'s a good day!')
print("Check\tthis\tout!")
print("This is a backslash: \\")

#formatted string
name = "John"
age = 23

#f-string
print(f'{name} is {age} years old')
print(f"{name} is {age} years old")

#format method. position based
print("{} is {:.4f} years old".format(name, age))
print("{1:.4f} is {0} years old".format(name, age))
# format method, keyword based
print("{y_name} is {y_age} years old".format(y_name=name, y_age=age))


#string is ordered sequence of characters
# index: 获取字符串中的某个字符
user_name = "Joe1234abc"
print(user_name[0])
print(user_name[len(user_name)-1])
# slice: 获取字符串中的一部分. [start:stop:step] , step 可以是负数，表示从右往左，这个时候 start 和 stop 也要调整， start 会比 stop 大。
print(user_name[0:5])
print(user_name[3:])
print(user_name[:5])
print(user_name[5:0:-2])


# string is inmutable
# user_name[0] = 'B' # this will raise an error : TypeError: 'str' object does not support item assignment