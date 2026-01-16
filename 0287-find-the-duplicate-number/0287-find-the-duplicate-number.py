class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        runner = 0

        while True:
            slow = nums[slow]
            runner = nums[runner]

            if slow == runner:
                return slow
                