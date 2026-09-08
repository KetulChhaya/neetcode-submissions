class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+','-','*','/']
        for t in tokens:
            if t in ops:
                pop1 = int(stack.pop()) if stack else 0
                pop2 = int(stack.pop()) if stack else 0
                res = 0
                if t == '+':
                    res = pop1 + pop2
                elif t == "-":
                    res = pop2 - pop1
                elif t == "*":
                    res = pop1 * pop2
                elif t == "/":
                    res = int(pop2 / pop1)
                stack.append(res)
            else:
                stack.append(t)
            
        return int(stack[-1])
        
            