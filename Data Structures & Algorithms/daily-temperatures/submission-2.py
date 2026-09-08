class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                ind = stack.pop()
                res[ind] = i - ind
            stack.append(i)
        return res