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
        
        # first find halway point
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        #slow pointer is at our halway point, everything after the slow pointer is the second list
        #pass in slow.next to reverse list, start from head of original list to slow
        #set slow.next to null

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
        l = head
        r = None
        while l:
            temp = l.next
            l.next = r
            r = l
            l = temp

        return r



