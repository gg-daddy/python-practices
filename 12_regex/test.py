import re


"""
re.match()：这个函数只匹配字符串的开始部分。
如果正则表达式在字符串的开始位置找不到匹配项，那么re.match()就会返回None。
即使在字符串的其他位置可以找到匹配项，re.match()也不会成功。
"""
result = re.match(r"Py", "Python")
print(result)  # <re.Match object; span=(0, 2), match='Py'>

"""
re.search()：这个函数会在整个字符串中查找匹配项。
只要字符串中的任何位置与正则表达式匹配，re.search()就会返回一个匹配对象。
如果在字符串中找不到匹配项，那么re.search()就会返回None。
"""
result = re.search(r"on", "Python")
print(result)  # <re.Match object; span=(4, 6), match='on'>

match = re.search(r"(\d+)-(\d+)-(\d+)", "2023-03-02")
print(match.groups())
if match:
    print(match.group(0))  # '2023-03-02'  ， 0 是整个匹配
    print(match.group(1))  # '2023'
    print(match.group(2))  # '03'
    print(match.group(3))  # '02'

"""
在Python的re模块中，以下是所有可用的flags：  
re.IGNORECASE或re.I：使匹配对大小写不敏感。
re.MULTILINE或re.M：使^和$匹配每一行的开始和结束，而不仅仅是整个字符串的开始和结束。
re.DOTALL或re.S：使.匹配任何字符，包括换行符。
re.VERBOSE或re.X：允许你在正则表达式中添加空格和注释，以提高其可读性。
re.ASCII或re.A：使\w, \W, \b, \B, \d, \D, \s和\S只匹配ASCII字符，而不是匹配Unicode字符。
re.LOCALE或re.L：使\w, \W, \b, \B和大小写敏感匹配受当前区域设置的影响。这个标志只对字节序列有用。
re.UNICODE或re.U：使\w, \W, \b, \B, \d, \D, \s和\S依赖于Unicode字符属性数据库。
这是默认设置，除非你在字节序列模式中提供了ASCII标志。
这些flags可以通过|操作符组合使用，例如flags=re.I | re.M。
"""
result = re.search(r"python", "PYTHON", flags=re.I)
print(result)  # <re.Match object; span=(0, 6), match='PYTHON'>
