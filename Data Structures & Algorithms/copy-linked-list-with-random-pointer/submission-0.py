"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        head_copy = head
        map_of_nodes = {}

        while(head_copy):
            map_of_nodes[head_copy] = Node(x=head_copy.val)
            head_copy = head_copy.next
        
        head_2_copy = head

        while(head_2_copy):
            map_of_nodes[head_2_copy].next = map_of_nodes.get(head_2_copy.next)
            map_of_nodes[head_2_copy].random = map_of_nodes.get(head_2_copy.random)
            head_2_copy = head_2_copy.next
        
        return map_of_nodes[head]
        
