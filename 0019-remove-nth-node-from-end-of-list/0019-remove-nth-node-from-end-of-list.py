# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse linked list then iterate runner to node before the nth node from the start
        reversedLinkedList = self.reverseLinkedList(head)
        if n == 1:
            reversedLinkedList = reversedLinkedList.next
        else:
            #prev is already at position 1
            prev = reversedLinkedList
            #need to stop at node before nth node, position = n - 1
            # (n - 1) - 1 = n - 2
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