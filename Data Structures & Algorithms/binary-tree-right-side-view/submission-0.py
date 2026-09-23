# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfsRight(self, root, level):
        if not root:
            return
        if level == len(self.ans):
            self.ans.append(root.val)
        self.dfsRight(root.right, level+1)
        self.dfsRight(root.left, level+1)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.dfsRight(root, 0)
        return self.ans