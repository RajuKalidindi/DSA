# Write a program to check if the given expression has balanced brackets in order.

def check_matching_brackets(expression):
    stack = []
    opening = ["(", "{", "["]
    closing = [")", "}", "]"]
    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if len(stack) == 0:
                print("Unbalanced")
                return
            if opening.index(stack.pop()) != closing.index(char):
                print("Unbalanced")
                return
    if len(stack) != 0:
        print("Unbalanced")
    else:
        print("Balanced")

expression = input("Enter the expression: ")
check_matching_brackets(expression)