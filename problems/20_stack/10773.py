class Stack:
    def __init__(self):
        self.items = []

    def sum(self):
        return sum(self.items)

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            return -1


stack = Stack()


def call_valid(call):
    if call == 0:
        stack.pop()
    else:
        stack.push(call)


calls = int(input())

for call in range(calls):
    input_call = int(input())
    call_valid(input_call)

print(stack.sum())
