
# Balanced Parentheses
# Parentheses are balanced, if all opening parentheses have their corresponding closing parentheses.

# Given an expression as input, we need to find out whether the parentheses are balanced or not.
# For example, "(x+y)*(z-2*(6))" is balanced, while "7-(3(2*9))4) (1" is not balanced.

# The problem can be solved using a stack.
# Push each opening parenthesis to the stack and pop the last inserted opening parenthesis whenever a closing parenthesis is encountered.
# If the closing bracket does not correspond to the opening bracket, then stop and say that the brackets are not balanced.
# Also, after checking all the parentheses, we need to check the stack to be empty -- if it's not empty, then the parentheses are not balanced.

# Implement the balanced() function to return True if the parentheses in the given expression are balanced, and False if not.

# Sample Input:
# (a( ) eee) )

# Sample Output:
# False

class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    else: 
        return False

s = Stack()
    
def balanced(expression):
    index = 0
    is_bal = True
    mystack = []

    for ex in expression:
        if ex in '()':
            mystack.append(ex)

    while index < len(mystack) an is_bal:
        paren = mystack[index]
        if paren == '(':
            s.push(paren)
        else:
            if s.is_empty():
                is_bal = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_bal = False
        index += 1

    if s.is_empty() and is_bal:
        return True
    else: 
        return False


print(balanced(input()))