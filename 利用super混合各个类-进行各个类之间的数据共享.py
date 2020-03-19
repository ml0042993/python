class Minix1:
    """该混合类为header列表末尾添加data1"""
    def get_header(self):
        print('run Minix1.get_header')
        ctx = super().get_header()
        ctx.append('data1')
        return ctx

class Minix2:
    """该混合类为header列表头部添加data2"""
    def get_header(self):
        print('run Minix2.get_header')
        ctx = super().get_header()
        ctx.insert(0, 'data2')
        return ctx

class Header:
    header = []
    def get_header(self):
        print('run Headers.get_header')
        return self.header if self.header else []


class Final(Minix1, Minix2, Header):
    def __init__(self):
        self.get_header()
    def get_header(self):
        return super().get_header()


obj = Final()
print(obj.get_header())
# class A1:
#     __head=['a','b']
#     def get_header(self):
#         print(self.__head)
# A1.__head = [111]
# obj = A1()
#
# obj.get_header()