class Base():
    def __init__(self,first,second):
        self.first=first
        self.second=second
        self.info()#子类的super()执行的此次会去调用子类的info,这是由于self指的是obj对象,而obj是子类的实例
    def info(self):
        print(self.first)
        print(self.second)
class Subclass(Base):
    def __init__(self,first,second,third,):
        self.third = third#该处的子类的变量要放在super()之前,
        super().__init__(first,second)
        self.info()
    def info(self):
        print(self.first)
        print(self.second)
        print(self.third)
obj = Subclass(1,2,3)
print(obj)