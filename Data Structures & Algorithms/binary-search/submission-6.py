class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self._binary_search(nums, target, 0, len(nums)-1)
    
    def _binary_search(self, nums: List[int], target: int, start: int, end: int) -> int:
        if start > end:
            return -1
        # elif start == end:
        #     return start if nums[start] == target else -1
        
        mid = (start + end) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            return self._binary_search(nums, target, start, mid-1)
        else:
            return self._binary_search(nums, target, mid+1, end)
