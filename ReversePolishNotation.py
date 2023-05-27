"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""

def evlRPN(token):
    
    stack = []
    for i in token:
        if i == "+":
            stack.append(stack.pop()+stack.pop())
        elif i == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif i == "*":
            stack.append(stack.pop()*stack.pop())
        elif i == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(int(a/b))
        else:
            stack.append(i)
    return stack[0]

print(evlRPN([2,1,"+",3,"*"]))