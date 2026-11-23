class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        total = [0] * (N+1)
        total[0] = 0
        total[1] = 0

        for i in range(2, N+1):
            total[i] = min(total[i-1] + cost[i-1], total[i-2] + cost[i-2])
        
        return total[N]