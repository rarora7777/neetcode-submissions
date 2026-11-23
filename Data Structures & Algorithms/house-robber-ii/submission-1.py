class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N==1:
            return nums[0]
        elif N==2:
            return max(nums[0], nums[1])
        else:
            return max(self.rob_helper(nums, 1, N), self.rob_helper(nums, 0, N-1))
    
    def rob_helper(self, nums: List[int], start, end) -> int:
        N = end - start
        max_total = [0] * N
        max_total[0] = nums[start]
        max_total[1] = max(nums[start], nums[start+1])

        for i in range(2, N):
            max_total[i] = max(max_total[i-1], nums[i+start] + max_total[i-2])
        
        return max_total[N-1]
        
        
