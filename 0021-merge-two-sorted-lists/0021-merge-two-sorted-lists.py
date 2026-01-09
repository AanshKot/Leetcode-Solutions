# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        runner1 = list1
        runner2 = list2

        newList = ListNode(-101)
        runner3 = newList
        #sorted in ascending order

        while runner1 and runner2:
            if runner1.val <= runner2.val:
                runner3.next = runner1
                runner1 = runner1.next
            else:
                runner3.next = runner2
                runner2 = runner2.next
            
            runner3 = runner3.next
        
        #if any list nodes remaining
        if runner2:
            runner3.next = runner2
        elif runner1:
            runner3.next = runner1
        
        return newList.next

        