class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.k_largest = []
        for n in nums:
            self.add(n)    

    def add(self, val: int) -> int:
        heapq.heappush(self.k_largest, val)
        if len(self.k_largest) > self.k:
            heapq.heappop(self.k_largest)
        return self.k_largest[0]
