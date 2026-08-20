class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1

        memo = {}
        memo[0] = 1
        memo[1] = 1
        
        def _climb(m: int):
            if memo.get(m):
                return memo[m]
            
            one = _climb(m-1)
            two = _climb(m-2)
            memo[m-1] = one
            memo[m-2] = two

            return one + two

        return _climb(n)