# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        curr = head
        while(curr and curr.next):
            next_node = curr.next

            # Only one node remains after curr
            if not next_node.next:
                break
            
            tail_prev = curr
            while(tail_prev.next.next):
                tail_prev = tail_prev.next
            tail = tail_prev.next
            tail_prev.next = None
            curr.next = tail
            tail.next = next_node
            curr = next_node
        