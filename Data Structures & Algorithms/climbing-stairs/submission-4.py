class Solution:

    def climbStairs(self, n: int) -> int:
        import numpy as np
        if n < 2:
            return 1

        def matpow(M, p):
            res = np.eye(2)
            base = M

            while p > 0:
                if p % 2 == 1:
                    res = res @ base
                base = base @ base
                p = p // 2
            
            return res
        
        M = np.array([[1, 1], [1, 0]])
        return int(matpow(M, n)[0, 0])



