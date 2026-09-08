class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(speed))]
        pairs.sort(reverse = True)
        fleet = 0
        max_time = 0
        for p,s in pairs:
            time = (target - p) / s
            if time > max_time:
                fleet += 1
                max_time = max(time, max_time)
        return fleet