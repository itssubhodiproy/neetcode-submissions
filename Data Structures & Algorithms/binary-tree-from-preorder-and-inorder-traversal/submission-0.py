# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, left, right):
        if left > right:
            return None
        root_val = preorder[self.root_idx]
        self.root_idx += 1
        root = TreeNode(root_val)
        mid = self.inorder_dict[root_val]
        root.left = self.dfs(left, mid-1)
        root.right = self.dfs(mid+1, right)
        return root
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorder_dict = {}

        for i in range(len(inorder)):
            self.inorder_dict[inorder[i]] = i

        self.root_idx = 0
        return self.dfs(0, len(inorder)-1)