class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N==1:
            return nums[0]
        elif N==2:
            return max(nums[0], nums[1])
        else:
            return max(self.rob_helper(nums[1:]), self.rob_helper(nums[:-1]))
    
    def rob_helper(self, nums: List[int]) -> int:
        N = len(nums)
        max_total = [0] * N
        max_total[0] = nums[0]
        max_total[1] = max(nums[0], nums[1])

        for i in range(2, N):
            max_total[i] = max(max_total[i-1], nums[i] + max_total[i-2])
        
        return max_total[N-1]
        
        
