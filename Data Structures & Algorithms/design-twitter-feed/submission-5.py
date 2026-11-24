class Twitter:

    def __init__(self):
        self._tweets = {}
        self._time = 0
        self._followers = {}
    
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

        self._time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Stupid edge-case: trying to get tweets from a user that has no tweets
        # and doesn't follow anyone
        if userId not in self._tweets:
            return []

        # This will be a max heap of valid tweets (from this user and their followers)
        # So we can pop to get the most recent (highest time) tweet first
        # The other option is to use a min heap and make sure it's length never exceeds 10
        # Then, reverse it and return
        heap = []
        
        # Add all tweets from the user themselves: O(log 10)
        for pair in self._tweets[userId]:
            heapq.heappush_max(heap, pair)

        # Add all tweets from followed accounts: O(10(n+1) log (10(n+1))) = O(n logn)
        for uid in self._followers[userId]:
            for pair in self._tweets[uid]:
                heapq.heappush_max(heap, pair)
        
        res = []
        # Pop from heap: O(1)
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
