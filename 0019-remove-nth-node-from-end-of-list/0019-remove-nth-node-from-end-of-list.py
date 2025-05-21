# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Move right n steps ahead
        for _ in range(n):
            right = right.next

        # Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next

        # Remove the node
        left.next = left.next.next

        return dummy.next