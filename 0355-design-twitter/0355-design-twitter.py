class Twitter:

    def __init__(self):
        # user adj list, representing users and their following
        # userId: [userIds] represents who the user is following
        self.users = {}

        # tweet adj list representing tuples with tweetId and timestamp, min heap ~ larger (more recent) timestamps need to be popped first 
        # userId -> tweetIds, timestamps
        self.tweets = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweets = self.tweets.get(userId, [])
        #append tweet as tuple with timestamp and tweetId
        tweets.append([-time.time(), tweetId])
        self.tweets[userId] = tweets


    def getNewsFeed(self, userId: int) -> List[int]:
        # for every user check their own tweet and their following user's tweets
        # append all tweets to a list and min heapify it?
        # with k = 10 select the

        # technically following yourself
        followingUserIds = self.users.get(userId, [userId])
        
        #match userIds to tweets
        tweetHistory = []
        
        print(f"user with id {userId} is following {followingUserIds}")
        for userId in followingUserIds:
            for tweet in self.tweets.get(userId, []):
                tweetHistory.append(tweet)
        
        heapq.heapify(tweetHistory)

        newsFeed = []
        # if user has len that 10 tweets in the tweetHistory
        for _ in range(min(10, len(tweetHistory))):
            newsFeed.append(heapq.heappop(tweetHistory)[1])
        
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        following = self.users.get(followerId, [followerId]) #user must follow themselves to see their own tweets

        if(followeeId in following):
            print(f"already following user with id: {followeeId}")
            return 

        following.append(followeeId)
        self.users[followerId] = following
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        following = self.users.get(followerId, [])

        if not following:
            print(f'already unfollowed user with id {followeeId}')
            return

        #O(n) time, n reps the number of followers the user with followeeId has 
        following.remove(followeeId)
        self.users[followerId] = following
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)