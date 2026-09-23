# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newNodeHead = ListNode() if list1 or list2 else None
        newNode = newNodeHead

        while(list1 and list2):
            if (list1.val <= list2.val):
                newNode.val = list1.val
                list1 = list1.next
            else:
                newNode.val = list2.val
                list2 = list2.next
            
            newNode.next = ListNode() if list1 or list2 else None
            newNode = newNode.next
        
        while(list1):
            newNode.val = list1.val
            list1 = list1.next
            newNode.next = ListNode() if list1 else None
            newNode = newNode.next
        
        while(list2):
            newNode.val = list2.val
            list2 = list2.next
            newNode.next = ListNode() if list2 else None
            newNode = newNode.next
        
        return newNodeHead