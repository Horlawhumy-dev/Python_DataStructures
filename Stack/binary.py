class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return 'Stack is empty!'

    def get_items(self):
        return self.items

def binary(dec_num):
    stack = Stack()
    while dec_num > 0:
        remainder = dec_num % 2
        stack.push(remainder)
        dec_num = dec_num // 2

    bin = " "
    while len(stack.get_items()) > 0:
        bin += str(stack.pop())
    return bin

decimal = int(input("Enter your decimal number: "))
print(binary(decimal))
