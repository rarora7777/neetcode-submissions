class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            cnt = count.get(n, 0) + 1
            count[n] = cnt

        for n, cnt in count.items():
            freq[cnt].append(n)
        
        top_k = [0] * k
        idx = 0
        for i in range(max(count.values()), 0, -1):
            for n in freq[i]:
                top_k[idx] = n
                idx += 1
                if idx == k:
                    return top_k

        return top_k