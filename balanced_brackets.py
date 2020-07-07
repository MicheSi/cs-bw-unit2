'''
Write function that take string as input. String can contain {}, [], (), ||
Function return boolean indicating whether or not string is balance
'''

table =  { ')': '(', ']':'[', '}':'{' }

for _ in range(int(input())):
    stack = []
    for x in input():
        if stack and table.get(x) == stack[-1]:
            stack.pop()
        else:
            stack.append(x)
    print("NO" if stack else "YES")


open_list = ["[","{","("] 
close_list = ["]","}",")"] 
  
# Function to check parentheses 
def check(myStr): 
    stack = [] 
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "Unbalanced"
    if len(stack) == 0: 
        return "Balanced"
    else: 
        return "Unbalanced"


def isBalanced(expr):
    if len(expr)%2!=0:
        return False
    opening=set('([{')
    match=set([ ('(',')'), ('[',']'), ('{','}') ])
    stack=[]
    for char in expr:
        if char in opening:
            stack.append(char)
        else:
            if len(stack)==0:
                return False
            lastOpen=stack.pop()
            if (lastOpen, char) not in match:
                return False
    return len(stack)==0


def is_matched(expression):
    if len(expression) % 2 != 0:
        return False

    opening = ("(", "[", "{")
    closing = (")", "]", "}")
    mapping = {opening[0]:closing[0],
               opening[1]:closing[1],
               opening[2]:closing[2]}

    if expression[0] in closing:
        return False

    if expression[-1] in opening:
        return False

    closing_queue = []
    for letter in expression:
        if letter in opening:
            closing_queue.append(mapping[letter])
        elif letter in closing:
            if not closing_queue:
                return False

            if closing_queue[-1] == letter:
                closing_queue.pop()
            else:
                return False

    return True