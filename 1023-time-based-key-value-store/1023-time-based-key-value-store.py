class TimeMap:
    
    def __init__(self):
        self.internalMap = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        #if no (value,timestamp) list is found in internalMap default to returning an empty array
        tupleList = self.internalMap.get(key, [])
        tupleList.append((value, timestamp))
        self.internalMap[key] = tupleList


    #timestamp = 5
    # tupleList [("high", 10), ("low", 20)]
    def get(self, key: str, timestamp: int) -> str:
        # look for first value that is less than or equal to provided timestamp
        tupleList = self.internalMap.get(key, [])

        low, high = 0, len(tupleList) - 1 # low = 0 , high = 1
        res = ""
        latestIndex = -1

        #when retrieving values by latest timestamp passed to `get`, need to binary search tuples since we know that all timestamps passed into `set` will be in increasing order
        # the array of tuples will be guaranteed to be in ascending order based on timestamp
        while low <= high:
            mid = (low + high) // 2

            value, prevTimestamp = tupleList[mid][0], tupleList[mid][1]

            if prevTimestamp > timestamp:
                high = mid - 1
        
            else:
                # mid will store the latest  prevTimestamp that is less than provided timestamp
                latestIndex = mid
                low = mid + 1
        
        if(latestIndex < 0):
            return res

        res =  tupleList[latestIndex][0] # low = 0, tupleList[-1][0]
        return res



        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)