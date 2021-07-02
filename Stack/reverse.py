
# this program reverses what string inputs given by user

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


# input from user
word = input('Enter your word: ')

# Initializing stack object
stack = Stack()

# function reversing a given word
def reverse_str(word):
    for i in range(len(word)):
      stack.push(word[i])

    rev = " "
    arr = stack.get_items()
    while len(arr) > 0:    
        rev += arr.pop()
    return rev 


print(reverse_str(word))
