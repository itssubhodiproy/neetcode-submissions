class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Convert first list to number
        num1 = ""
        while l1:
            num1 += str(l1.val)
            l1 = l1.next

        # Convert second list to number
        num2 = ""
        while l2:
            num2 += str(l2.val)
            l2 = l2.next

        total = int(num1[::-1]) + int(num2[::-1])
        digits = str(total)[::-1]

        # Convert result back to linked list
        dummy = ListNode()
        curr = dummy

        for digit in digits:
            curr.next = ListNode(int(digit))
            curr = curr.next

        return dummy.next