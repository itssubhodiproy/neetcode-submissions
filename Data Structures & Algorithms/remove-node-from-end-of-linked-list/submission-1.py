class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Remove head
        if n == length:
            return head.next

        # Find node before the one to remove
        curr = head
        for _ in range(length - n - 1):
            curr = curr.next

        curr.next = curr.next.next

        return head