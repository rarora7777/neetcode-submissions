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
        
        heapq.heappush(self._tweets[userId], (self._time, tweetId))
        while len(self._tweets[userId]) > 10:
            heapq.heappop(self._tweets[userId])

        self._time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self._tweets:
            return []

        heap = []
        for pair in self._tweets[userId]:
            heapq.heappush_max(heap, pair)

        for uid in self._followers[userId]:
            for pair in self._tweets[uid]:
                heapq.heappush_max(heap, pair)
        res = []
        while heap and len(res) < 10:
            res.append(heapq.heappop_max(heap)[1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self._create_user(followerId)
        self._create_user(followeeId)
        
        self._followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self._followers[followerId]:
            self._followers[followerId].remove(followeeId)
