class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        top_k = []
        for n in nums:
            heapq.heappush(top_k, n)
            if len(top_k) > k:
                heapq.heappop(top_k)
            # print(top_k)
        
        return top_k[0]