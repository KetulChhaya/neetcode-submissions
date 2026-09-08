class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {'}': '{', ')': '(', ']': '['}

        for i in range(len(s)):
            if s[i] in bracket_map.values():
                stack.append(s[i])
            elif s[i] in bracket_map:
                if not stack or stack.pop() != bracket_map[s[i]]:
                    return False
            
        return not stack