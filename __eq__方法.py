# class A(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __eq__(self, obj):
#         return self.name == obj.name
#     def __hash__(self):
#         return
#
# if __name__ == '__main__':
#     a = A("Leon")
#     b = A("Leon")
#     print(a == b)
#     print(id(a),id(b))


class Foo:
    def __init__(self, item):
        self.item = item

    def __eq__(self, other):
        print('使用了equal函数的对象的id',id(self))
        if isinstance(other, self.__class__):
            print(self.__class__.__name__,other.__class__)
            return self.__dict__ == other.__dict__
        else:
            return False
    def __hash__(self):
        print('f'+str(self.item)+'使用了hash函数')
        return hash(self.item)
f1 = Foo(1)
f2 = Foo(2)
f3 = Foo(3)
fset = set([f1, f2, f3])
print(fset)
print(type(fset))
f = Foo(3)
fset.add(f)
# print('f3的id:',id(f3))
# print('f的id:',id(f))

print(f2.__dict__)


it = ['a','b','c']
initial = ['zhou','li']
dic = {}

dic.fromkeys(it,['zhou'])

print(dic.fromkeys(it,word for word in initial)
