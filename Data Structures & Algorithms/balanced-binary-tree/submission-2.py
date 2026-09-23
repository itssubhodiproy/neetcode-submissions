# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return 0
        left_height = self.dfs(root.left)
        right_height = self.dfs(root.right)
        if(left_height==-1 or right_height==-1):
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return 1 + max(left_height, right_height)
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # self.ans = True
        if self.dfs(root) == -1:
            return False
        else:
            return True
        # return self.ans
        