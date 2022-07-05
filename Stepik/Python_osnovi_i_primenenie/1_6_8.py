class ExtendedStack(list):
    def pops(self):
        return self.pop()

    def sum(self):
        self.append(self.pops() + self.pops())
        self.show()

    def sub(self):
        self.append(self.pops() - self.pops())
        self.show()

    def mul(self):
        self.append(self.pops() * self.pops())
        self.show()

    def div(self):
        self.append(self.pops() // self.pops())
        self.show()

    def show(self):
        print(self)


'''
class ExtendedStack(list):
    def sum(self):
        self.append(self.pop() + self.pop())
        self.show()

    def sub(self):
        self.append(self.pop() - self.pop())
        self.show()

    def mul(self):
        self.append(self.pop() * self.pop())
        self.show()

    def div(self):
        self.append(self.pop() // self.pop())
        self.show()

    def show(self):
        print(self)
'''


def test():
    ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
    ex_stack.show()
    ex_stack.div()
    assert ex_stack.pop() == 2
    ex_stack.sub()
    assert ex_stack.pop() == 6
    ex_stack.sum()
    assert ex_stack.pop() == 7
    ex_stack.mul()
    assert ex_stack.pop() == 2
    assert len(ex_stack) == 0


test()