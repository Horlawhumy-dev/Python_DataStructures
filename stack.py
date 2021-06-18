# How Stack Data Structures work in Python
import random
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

# my_stack = Stack()
# print(my_stack.is_empty())
# my_stack.push('Blue')
# my_stack.push(True)
# my_stack.push(100)
# my_stack.push('Green')
# my_stack.push('Red')
# print(my_stack.get_items())
# print(my_stack.pop())
# print(my_stack.get_items())

# # Getting element of the stack
# elements = my_stack.get_items()
# for el in elements:
#     id = random.randint(0, 101)
#     dict = {id: el}
#     my_stack.push(dict)
# print(my_stack.get_items())