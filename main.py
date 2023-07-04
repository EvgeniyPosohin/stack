import Stack


def chek(object):
    dict_staples = {'(': ')',
                    '{': '}',
                    '[': ']'}
    if object in dict_staples.keys():
        stack.push(object)
    elif object in dict_staples.values() and\
            dict_staples[stack.peek()] == object:
        stack.pop()
    else:
        return


def balancing(staples):
    if len(staples) % 2 == 0:
        for object in staples:
            chek(object)
        if stack.size():
            print('Несбалансирован')
        else:
            print('сбалансирован')
    else:
        print('Несбалансирован')


if __name__ == '__main__':
    stack = Stack.Stack()
    balancing('([]{}())')
    balancing('((({{{[]}}})))')
    balancing('[[{(())}]')
    balancing('[([])((([[[]]])))]{()}')

