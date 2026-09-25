# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # traverse the 1st list and do everything
        string1st = ""

        while(l1):
            string1st += str(l1.val)
            l1 = l1.next
        
        string1st = string1st[::-1]
        string1st = int(string1st)

        # traverse the 2nd list and do everything

        string2nd = ""

        while(l2):
            string2nd += str(l2.val)
            l2 = l2.next
        
        string2nd = string2nd[::-1]
        string2nd = int(string2nd)

        # computing ans
        val = string1st+string2nd

        val = str(val)
        val = val[::-1]

        prev = ListNode(val=int(val[0]))
        head = prev
        curr = None

        for c in val:
            curr = ListNode(val=int(c))
            prev.next = curr
            prev = curr
        
        return head.next
             
        





