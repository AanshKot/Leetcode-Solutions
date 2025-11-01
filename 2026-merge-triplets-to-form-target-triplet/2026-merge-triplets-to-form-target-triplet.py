class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # if we cannot match a value in target the length < 3
        good = set() #the index's that have a matched value in target 

        for t in triplets:
            # if any of the values in the triplet are greater than the target its impossible to use this triplet to form the target
            # remember we are taking the max at each individual index
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            for i,v in enumerate(t):
                if v == target[i]:
                    good.add(i)
            
        if len(good) == 3:
            return True
        
        return False
        
        