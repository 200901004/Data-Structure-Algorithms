#balanced
from collections import deque
class balanced:
    stack=[]
    def __init__(self):
        self.stack=deque()
    def push(self,paren):
        self.stack.append(paren)
    def pop(self):
        return self.stack.pop()
        
    def check_balanced(self,equation):   
        for paren in equation:
            if paren in ["(","{","["]:
                self.push(paren)
            else:
                if not self.stack: 
                    return False 
                parenthesis=self.pop()
                if parenthesis=="(":
                    if paren!=")":
                        return False
                if parenthesis=="{":
                    if paren!="}":
                        return False
                if parenthesis=="[":
                    if paren!="]":
                        return False
        if self.stack:
            return False
        return True
b=balanced()
paren=input("Enter the equation: ")
if b.check_balanced(paren):
        print(paren,"- Balanced")
else:
        print(paren,"- Unbalanced")       
        
