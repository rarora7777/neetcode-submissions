class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1
        if m < n:
            m, n = n, m
        
        # Now we need to compute (m+n)! / (m! n!), with m >= n
        # Which is the same as 
        #   (1 * 2 * ... m+n) / ( (1 * 2 * ... m) * (1 * 2 * ... n) )
        # = (m+1 * m+2 * ... m+n) / (1 * 2 * ... n)
        # = Π_{k = 1 to n} (m+k / k)
        res = 1
        for k in range(1, n+1):
            res = res * (m+k)
            # res has now been multiplied by k consecutive integers: m+1, m+2, ..., m+k
            # since at least one of these must be divisible by k, we can safely divide
            # res by k without any rounding
            res = res // k

        return res
