class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # have an additional 0 at the end just to make math work out

        cost.append(0)

        #bottom up solution
        #iterate through array in reverse order
        #not going to be changing (technical last value in cost index)
        # start at second last index
        # remember have appended 0 to the cost array to represent the out of bounds cost
        for i in range(len(cost) - 3, -1, -1):
            #first choice if we make a single jump
            # second choice if we make a double jump
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])
        
        # guaranteed cost array has atleast 2 values
        return min(cost[0], cost[1])



        