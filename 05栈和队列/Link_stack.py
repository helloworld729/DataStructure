class LinkStackError(ValueError):
    pass


class Lnode():
    def __init__(self, elem, next=None):
        self._elem = elem
        self._next = next

class LinkStack():
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self, elem):
        node = Lnode(elem, self._top)
        self._top = node

    def pop(self):
        if self.is_empty():
            raise LinkStackError
        else:
            ele = self._top._elem
            self._top = self._top._next
            return ele

    def top(self):
        return self._top._elem


lstack = LinkStack()
for i in range(5):
    lstack.push(i)
for i in range(5):
    print(lstack.pop(), end=' ')