class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return False
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if stack and mapping[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True
        