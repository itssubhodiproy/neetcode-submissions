# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        ans = []
        if not root:
            return ans
        
        q.append(root)

        while q:
            level = len(q)
            temp = []

            while level:
                top = q.popleft()

                if top.left:
                    q.append(top.left)
                
                if top.right:
                    q.append(top.right)
                
                temp.append(top.val)
                level -= 1

            ans.append(temp)

        return ans