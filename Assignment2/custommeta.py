"""
Hometask №2: Making a custom metaclass
"""
class CustomMeta(type):
    def __setattr__(cls, name, value):
        print(cls.__dict__["custom_" + name])
        cls.__dict__["custom_" + name] = value


    def __new__(cls, name, bases, namespace):
        new_namespace = {}
        for key in namespace:
            if not (key.startswith('__') and key.endswith('__')):
                new_namespace["custom_" + key] = namespace[key]
            else:
                new_namespace[key] = namespace[key]
        namespace = new_namespace
        return super().__new__(cls, name, bases, namespace)

class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val #call

    def line(self):
        return 100

inst = CustomClass()
#print(inst.custom_x)
#print(inst.custom_val)
#print(inst.custom_line())