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

        # Create a dummy head node. This simplifies handling the first node
        # of the result list, as we can always append to dummy_head.next.
        dummy_head = ListNode()
        # Initialize a pointer to the current node in the result list.
        current = dummy_head
        # Initialize the carry-over value from one digit position to the next.
        carry = 0

        # Loop as long as there are digits in either list or there's a carry.
        # This ensures all digits are processed and any final carry is added.
        while l1 or l2 or carry:
            # Get the value of the current digit from l1. If l1 is None, treat it as 0.
            val1 = l1.val if l1 else 0
            # Get the value of the current digit from l2. If l2 is None, treat it as 0.
            val2 = l2.val if l2 else 0

            # Calculate the sum of the current digits and the carry from the previous position.
            sum_digits = val1 + val2 + carry

            # The new carry is the quotient when sum_digits is divided by 10.
            carry = sum_digits // 10
            # The digit for the current position is the remainder when sum_digits is divided by 10.
            digit = sum_digits % 10

            # Create a new ListNode with the calculated digit.
            new_node = ListNode(digit)
            # Attach this new node to the 'next' of the current node in the result list.
            current.next = new_node
            # Move the 'current' pointer to the newly added node.
            current = new_node

            # Move to the next nodes in l1 and l2, if they exist.
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # The result list starts from dummy_head.next, as dummy_head itself was just a placeholder.
        return dummy_head.next

