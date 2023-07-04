class Stack:
    def __init__(self):
        self.obj = []

    def is_empty(self):
        return bool(self.obj)

    def push(self, element):
        self.obj.append(element)

    def pop(self):
        return self.obj.pop(-1)

    def __repr__(self):
        print(f'{self.obj!r}')

    def peek(self):
        return self.obj[-1]

    def size(self):
        return len(self.obj)




