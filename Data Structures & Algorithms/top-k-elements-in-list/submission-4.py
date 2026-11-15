class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        sorted_count = sorted(count.items(), key=lambda item: -item[1])

        return [k for k, v in sorted_count[:k]]