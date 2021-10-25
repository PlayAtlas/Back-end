"""
Hometask №2: Making a custom metaclass
"""
class CustomMeta(type):
    """def __init__(cls):
        def __setattr__(cls, name, value):
            print(cls.__dict__["custom_" + name])
            cls.__dict__["custom_" + name] = value
        return super().__init__(cls)"""
    def __call__(cls):
        """def __setattr__(cls, name, value):
            print('--setattr--\n\n\n')
            print(cls.__dict__["custom_" + name])
            cls.__dict__["custom_" + name] = value"""
        obj = type.__call__(cls)
        namespace = obj.__dict__
        #print(namespace)
        new_namespace = {}
        for key in namespace:
            if not (key.startswith('__') and key.endswith('__')):
                new_namespace["custom_" + key] = namespace[key]
            else:
                new_namespace[key] = namespace[key]
        obj.__dict__ = new_namespace
        #print(new_namespace)
        return obj


    def __new__(cls, name, bases, namespace):
        new_namespace = {}
        for key in namespace:
            if not (key.startswith('__') and key.endswith('__')):
                new_namespace["custom_" + key] = namespace[key]
            else:
                new_namespace[key] = namespace[key]
        return super().__new__(cls, name, bases, new_namespace)

class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val #call

    def line(self):
        return 100

inst = CustomClass()
print(inst)
#print(inst.custom_x)
#print(inst.custom_val)
#print(inst.custom_line())