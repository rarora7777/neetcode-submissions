class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = zip(position, speed)
        pairs = sorted(pairs)

        collisions = 0
        if len(pairs) <= 1:
            return len(pairs)

        t1 = (target - pairs[-1][0]) / pairs[-1][1]
        for i in range(len(pairs)-2, -1, -1):
            p0, v0 = pairs[i]
            t0 = (target - p0) / v0
            if t0 <= t1:
                collisions += 1
            else:
                t1 = t0
        
        return len(pairs) - collisions
        