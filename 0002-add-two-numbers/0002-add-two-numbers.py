# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        runner1 = l1
        runner2 = l2

        num1 = ""
        num2 = ""
        
        while runner1:
            num1 += str(runner1.val)
            runner1 = runner1.next
        
        while runner2:
            num2 += str(runner2.val)
            runner2 = runner2.next
        
        firstNum = int(num1[::-1])
        secondNum = int(num2[::-1])

        sumStr = str(firstNum + secondNum)
        reversedSum = sumStr[::-1]

        dummy = ListNode()
        runner = dummy
        for i in reversedSum:
            runner.next = ListNode(int(i))
            runner = runner.next
        
        return dummy.next




        

        