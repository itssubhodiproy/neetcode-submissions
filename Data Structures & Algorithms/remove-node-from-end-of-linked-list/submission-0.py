# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        # length calculation
        length = 0
        copy_head = head
        while(copy_head):
            length+=1
            copy_head = copy_head.next
        if length == 1:
            return None
        n = length-n+1

        curr = head
        prev = head

        if n == 1:
            return prev.next
        
        count = 1
        while(prev.next):
            if count+1 == n:
                prev.next = prev.next.next
                break
            prev = prev.next
            count += 1
        return head

