class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(speed))]
        pairs.sort(reverse = True)
        fleet = 0
        stack = []
        for pos, speed in pairs:
            time = (target - pos)/speed
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        # max_time = 0
        # for p,s in pairs:
        #     time = (target - p) / s
        #     if time > max_time:
        #         fleet += 1
        #         max_time = time
        # return fleet