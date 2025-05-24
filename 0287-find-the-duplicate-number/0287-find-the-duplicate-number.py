class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #start at 0, 0 is never going to be part of the cycle
        slow, fast = 0, 0

        while True:
            #slow, fast always going to be in bounds
            slow = nums[slow]
            fast = nums[nums[fast]] #advance fast by two

            #when slow and fast intersect
            if slow == fast:
                break
        
        #start point to beginning of cycle, advance point to original point where slow and fast intersect (slow)
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow
           