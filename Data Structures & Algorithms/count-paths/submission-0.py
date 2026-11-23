class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            m, n = n, m
        # Now, m <= n
        m_fact = self.prod(1, m) # (m-1)!
        sum_fact_over_n_fact = self.prod(n, m+n-1) #(m-1+n-1)! / (n-1)!

        return int(sum_fact_over_n_fact / m_fact)


    def prod(self, start: int, end: int) -> int:
        res = 1
        for i in range(start, end):
            res *= i
        
        return res
