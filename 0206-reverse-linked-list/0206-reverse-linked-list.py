# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = None
        right = head

        while right:
            temp = right.next
            right.next = left
            left = right
            right = temp
        
        #left ends up at the end of the linked list
        return left


