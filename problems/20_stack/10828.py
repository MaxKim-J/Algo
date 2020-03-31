class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            return -1

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            return -1

    def empty(self):
        if len(self.items) == 0:
            return 1
        else:
            return 0


stack = Stack()
results = []
map_dict = {"top": stack.top(), "size": stack.size(),
            "empty": stack.empty(), "pop": stack.pop()}


def order_valid(order):
    if " " in order:
        order_processed = order.split(" ")
        stack.push(order_processed[1])
    else:
        results.append(map_dict[order])


orders = int(input())
for chance in range(orders):
    input_order = input()
    order_valid(input_order)

for result in results:
    print(result)
