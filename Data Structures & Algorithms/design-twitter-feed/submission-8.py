class Twitter:

    def __init__(self):
        # Space taken for each data structure
        # O (N * m): N lists, each of size at most m
        self._tweets: list[list[int]] = {}
        # O (N * M): N lists, each of size at most M
        self._followers: list[set[int]] = {}
        # O(1): just an integer
        self._time: int = 0
    
    def _create_user(self, userId: int):
        if userId not in self._tweets:
            self._tweets[userId] = []
            self._followers[userId] = set()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._create_user(userId)
        
        # Push tweet onto min-heap sorted by time, so the oldest (least recent)
        # is popped first.
        heapq.heappush(self._tweets[userId], (self._time, tweetId))
        # Only keep the most recent 10 tweets by popping the oldest one
        if len(self._tweets[userId]) > 10:
            heapq.heappop(self._tweets[userId])

        # Since each push and pop from a heap of size k is O(logk), and this function
        # calls a single push and at most one pop on heap of size at most 11, total
        # time complexity is O(2 * 11) = O(1)
        self._time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Stupid edge-case: trying to get tweets from a user that has no tweets
        # and doesn't follow anyone
        if userId not in self._tweets:
            return []

        # This will be a max heap of valid tweets (from this user and their followers)
        # So we can pop to get the most recent (highest time) tweet first
        heap = []
        
        # Add all tweets from the user themselves: O(10 log 10) = O(1)
        for pair in self._tweets[userId]:
            heapq.heappush_max(heap, pair)

        # Add all tweets from followed accounts: O(10(n+1) log (10(n+1))) = O(n logn)
        for uid in self._followers[userId]:
            for pair in self._tweets[uid]:
                heapq.heappush_max(heap, pair)
        
        res = []
        # Each pop from heap is O(log n), with at most 10 pops in total.
        while heap and len(res) < 10:
            res.append(heapq.heappop_max(heap)[1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self._create_user(followerId)
        self._create_user(followeeId)
        
        # Adding to a set is O(1)
        self._followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Checking existence in a set is O(1)
        if followeeId in self._followers[followerId]:
            # Removing from a set is O(1)
            self._followers[followerId].remove(followeeId)
