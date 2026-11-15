class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        max_count = 0
        for n in nums:
            count[n] = count.get(n, 0) + 1
            max_count = max(max_count, count[n])

        for n, cnt in count.items():
            freq[cnt].append(n)
        
        top_k = []
        for i in range(max_count, 0, -1):
            for n in freq[i]:
                top_k.append(n)
                if len(top_k) == k:
                    return top_k

        return top_k