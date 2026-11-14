class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {i: 0 for i in range(3)}

        for n in nums:
            count[n] += 1
        
        n = 0
        for i in range(len(nums)):
            while count[n] == 0:
                n += 1
            nums[i] = n
            count[n] -= 1
        
        return
        
# count: {0: 1, 1: 2, 2: 1}
# [0, 1, 1, 2]
# i = 0, nums[0] = 0, count[0] = 0