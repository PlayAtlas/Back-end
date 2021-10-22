class CustomList(list):
    def __add__(self, other):
        sum = CustomList()
        if len(self) >= len(other):
            for i in range(len(other)):
                sum.append(self[i] + other[i])
            for i in range(len(other), len(self)):
                sum.append(self[i])
        else:
            for i in range(len(self)):
                sum.append(self[i] + other[i])
            for i in range(len(self), len(other)):
                sum.append(other[i])
        return sum

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        dif = CustomList()
        if len(self) >= len(other):
            for i in range(len(other)):
                dif.append(self[i] - other[i])
            for i in range(len(other), len(self)):
                dif.append(self[i])
        else:
            for i in range(len(self)):
                dif.append(self[i] - other[i])
            for i in range(len(self), len(other)):
                dif.append(-other[i])
        return dif

    def __rsub__(self, other):
        return self - other

    def __lt__(self, other):
        val1 = sum(self)
        val2 = sum(other)
        return val1 < val2

    def __le__(self, other):
        val1 = sum(self)
        val2 = sum(other)
        return val1 <= val2

    def __eq__(self, other):
        val1 = sum(self)
        val2 = sum(other)
        return val1 == val2

    def __ne__(self, other):
        val1 = sum(self)
        val2 = sum(other)
        return val1 != val2

    def __gt__(self, other):
        val1 = sum(self)
        val2 = sum(other)
        return val1 > val2

    def __ge__(self, other):
        val1 = sum(self)
        val2 = sum(other)
        return val1 >= val2




