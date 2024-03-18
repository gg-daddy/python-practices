class A:
    def process(self):
        print('A process()')


class B:
    def process(self):
        print('B process()')


class C(A, B):
    pass


obj = C()
obj.process()

# 下面两种方式是等价的。
# MRO: Method Resolution Order
print(C.mro())
print(C.__mro__)

# Refer: http://www.srikanthtechnologies.com/blog/python/mro.aspx
