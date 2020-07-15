class StackflowError(ValueError):
    pass


class Stack():
    def __init__(self):
        self._elem = []

    def is_empty(self):
        return len(self._elem ) == 0

    def push(self, elem):
        self._elem.append(elem)
        return

    def pop(self):
        if self.is_empty():
            raise StackflowError('UnderFlowError')
        else:
            return self._elem.pop()

    def top(self):
        if self.is_empty():
            raise StackflowError('UnderFlowError')
        else:
            return self._elem[-1]

    def elements(self):  # 按照FILO的顺序返回
        while not self.is_empty():
            yield self.pop()


# if __name__ == '__main__':
#     stack = Stack()
#     for i in range(5):
#         stack.push(i)
#
#     for ele in stack.elements():
#         """此处是倒叙输出，也算是栈的一个应用"""
#         print(ele, end=' ')