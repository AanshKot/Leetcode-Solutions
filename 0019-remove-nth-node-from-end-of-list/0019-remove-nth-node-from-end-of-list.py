# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        reversedLinkedList = self.reverseLinkedList(head)
        if n == 1:
            reversedLinkedList = reversedLinkedList.next
        else:
            prev = reversedLinkedList
            for _ in range(n - 2):
                prev = prev.next

            prev.next = prev.next.next

        return self.reverseLinkedList(reversedLinkedList)

    def reverseLinkedList(self, head):
        runner = head
        left = None
        
        while runner:
            temp = runner.next
            runner.next = left
            left = runner
            runner = temp
        return left