class SuperList(list):
    def __init__(self, val):
        self.val = val
    def __add__(val, other: list):
        return super().__add__(other)

class CustomList(metaclass=SuperList):
    pass

mysuperlist1 = CustomList()

