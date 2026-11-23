class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 or n==1:
            return 1
        m -= 1
        n -= 1
        if m < n:
            m, n = n, m
        
        # Now we need to compute (m+n)! / (m! n!), with m >= n
        res = 1
        for k in range(1, n+1):
            res *= (m+k)
            res //= k

        return res
