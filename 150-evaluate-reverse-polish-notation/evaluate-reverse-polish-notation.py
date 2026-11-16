import math

class Solution(object):
    def evalRPN(self, tokens):
        symbols = ['+', '-', '*', '/']
        stack = []

        for token in tokens:
            if token in symbols:
                second_digit = int(stack.pop())
                first_digit = int(stack.pop())

                if token == '+':
                    add = first_digit + second_digit
                    print(add)
                    stack.append(add)

                elif token == '-':
                    sub = first_digit - second_digit
                    print(sub)
                    stack.append(sub)

                elif token == '*':
                    multi = first_digit * second_digit
                    print(multi)
                    stack.append(multi)

                else:
                    div = first_digit//second_digit if first_digit*second_digit >= 0 else -(-first_digit//second_digit)
                    print(div)
    
                    stack.append(div)

            else:
                stack.append(token)

        return int(stack[-1])



