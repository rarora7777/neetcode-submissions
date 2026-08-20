class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1

        x0 = 0
        x1 = 1
        x2 = 1

        i = 1
        while i <= n:
            x2 = x0 + x1
            x0 = x1
            x1 = x2
            i += 1
        
        return x2