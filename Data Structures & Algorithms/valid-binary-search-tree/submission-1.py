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
        
        if root.val<=min_val:
            return False
        
        if root.val>=max_val:
            return False
        
        left = self.dfs(root.left, min_val, min(max_val, root.val))
        right = self.dfs(root.right, max(min_val, root.val), max_val)

        if not left or not right:
            return False
        
        return True

        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min_val = -1001
        max_val = 1001

        return self.dfs(root, min_val, max_val)

