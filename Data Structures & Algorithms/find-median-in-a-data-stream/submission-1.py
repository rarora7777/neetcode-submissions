class MedianFinder:

    def __init__(self):
        # small is a max heap with n//2 elements
        # large is a min heap with n - n//2 elements
        # if n is odd, median = min(large)
        # if n is even, median = (min(large) + max(small))/2
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.large) == 0 or num >= self.large[0]:
            heapq.heappush(self.large, num)
            while len(self.large) - len(self.small) > 1:
                x = heapq.heappop(self.large)
                heapq.heappush_max(self.small, x)
        else:
            heapq.heappush_max(self.small, num)
            while len(self.small) > len(self.large):
                x = heapq.heappop_max(self.small)
                heapq.heappush(self.large, x)
        # print(f"Added {num}")
        # print(f"Large: {self.large}")
        # print(f"Small: {self.small}")
        
    def findMedian(self) -> float:
        n = len(self.large) + len(self.small)
        # assert n > 0
        if n % 2 == 1:
            return self.large[0]
        else:
            return (self.large[0] + self.small[0]) * 0.5
        