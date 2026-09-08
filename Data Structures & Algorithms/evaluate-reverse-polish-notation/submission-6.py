class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        mapping = {'+', '-', '*', '/'}
        for c in tokens:
            if c not in mapping:
                stack.append(c)
            else:
                if len(stack) >= 2:
                    op2 = int(stack.pop())
                    op1 = int(stack.pop())
                    res = -1
                    if c == '+':
                            res = op1 + op2   
                    elif c == '-':
                        res = op1 - op2
                    elif c == '*':
                        res = op1 * op2
                    elif c == '/':
                        res = op1 /op2
                    stack.append(res)
        return int(stack[-1])

