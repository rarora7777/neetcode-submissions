class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        
        max_total = [0] * N
        max_total[0] = nums[0]
        max_total[1] = max(nums[0], nums[1])

        for i in range(2, N):
            max_total[i] = max(max_total[i-1], nums[i] + max_total[i-2])
        
        return max_total[N-1]


