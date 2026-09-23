# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs (self, root):
        if not root:
            return 0
        left = max(0, self.dfs(root.left))
        right = max(0, self.dfs(root.right))
        total = root.val + left + right
        self.global_max = max(self.global_max, total)
        return root.val + max(left, right)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max = -1001
        self.dfs(root)
        return self.global_max