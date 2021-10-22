class CustomMeta(type):
    def __new__(cls, name, bases, namespace):#надо
        #cls.custom_x = CustomClass.x
        for key, value in namespace:#надо проитерироваться и поменять
        print(namespace)#для понимания
        return super().__new__(cls, name, bases, namespace)#тоже надо

class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val #call

    def line(self):
        return 100

inst = CustomClass()
print(inst.custom_x)
print(inst.custom_val)
print(inst.custom_line())

#inst.x  # ошибка
#inst.val  # ошибка
#inst.line() # ошибка