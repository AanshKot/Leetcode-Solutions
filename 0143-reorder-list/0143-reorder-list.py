# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        slow = head
        fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        #slow is at the midpoint
        temp = slow.next
        slow.next = None
        reversedList = self.reverseList(temp)

        listRunner = head
        
        while listRunner and reversedList:
            temp = listRunner.next
            listRunner.next = reversedList
            listRunner = listRunner.next
            reversedList = reversedList.next
            listRunner.next = temp
            listRunner = listRunner.next

        return head

    def reverseList(self, head):
        listRunner = head

        left = None

        while listRunner:
            temp = listRunner.next
            listRunner.next = left
            left = listRunner
            listRunner = temp
        
        return left