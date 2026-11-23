class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        total = [0] * (N+1)
        total[0] = 0
        total[1] = cost[0]

        for i in range(2, N+1):
            total[i] = cost[i-1] + min(total[i-1], total[i-2])
        
        return min(total[N], total[N-1])