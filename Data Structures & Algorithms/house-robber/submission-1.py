class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        total = [0] * N
        total[0] = nums[0]
        total[1] = nums[1]
        
        max_total = [0] * N
        max_total[0] = nums[0]
        max_total[1] = max(nums[0], nums[1])

        for i in range(2, N):
            total[i] = nums[i] + max_total[i-2]
            max_total[i] = max(total[i], max_total[i-1])
        
        return max(total[N-1], total[N-2])


