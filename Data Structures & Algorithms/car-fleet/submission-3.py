class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        collisions = 0
        if len(pairs) <= 1:
            return len(pairs)

        t1 = (target - pairs[0][0]) / pairs[0][1]
        for i in range(1, len(pairs)):
            p0, v0 = pairs[i]
            t0 = (target - p0) / v0
            if t0 <= t1:
                collisions += 1
            else:
                t1 = t0
        
        return len(pairs) - collisions
        