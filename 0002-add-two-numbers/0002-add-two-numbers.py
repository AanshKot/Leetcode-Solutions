# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummyNode = ListNode()
        cur = dummyNode
        carry = 0

        while l1 or l2 or carry:
            firstDigit = l1.val if l1 else 0
            secondDigit = l2.val if l2 else 0

            sumDigits = firstDigit + secondDigit + carry

            carry = sumDigits // 10
            curDigit = sumDigits % 10


            newNode = ListNode(curDigit)
            cur.next = newNode
            
            cur = cur.next
            # Move to the next nodes in l1 and l2, if they exist.
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummyNode.next