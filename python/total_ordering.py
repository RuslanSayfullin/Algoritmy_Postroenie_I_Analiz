class BaseClass:
    @total_ordering
    def __init__(self, a):
        self.a = a

    def __eq__(self, other):
        return self.a == other.a


class MyClass(BaseClass):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def __lt__(self, other):
        return self.b < other.b
