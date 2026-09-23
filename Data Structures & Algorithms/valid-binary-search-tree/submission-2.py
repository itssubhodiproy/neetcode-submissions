# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, min_val, max_val):
        if not root:
            return True
        
        if root.val<=min_val or root.val>=max_val:
            return False
        
        left = self.dfs(root.left, min_val, root.val)
        right = self.dfs(root.right, root.val, max_val)

        return left and right
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, -1001, 1001)

