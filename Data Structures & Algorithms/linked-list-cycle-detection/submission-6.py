# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        fast_ptr = None
        if head.next:
            fast_ptr = head.next.next
        slow_ptr = head.next


        while fast_ptr:
            if fast_ptr == slow_ptr:
                return True

            if fast_ptr.next:
                fast_ptr = fast_ptr.next.next
            else:
                fast_ptr = None

            slow_ptr = slow_ptr.next

        return False