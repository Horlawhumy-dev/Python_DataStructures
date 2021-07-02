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

num = int(input('Enter your number: '))

def print_prime(num):
    stack = Stack()
    if num >= 10: 
        for n in range(num):
            stack.push(n)
    else:
        print('Number cannot be less than 10')
    return stack.get_items()

print(print_prime(num))
