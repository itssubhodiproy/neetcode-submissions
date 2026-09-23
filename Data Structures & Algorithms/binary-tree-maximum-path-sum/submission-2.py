class Solution:
    def dfs(self, root):
        if not root:
            return 0

        left = max(0, self.dfs(root.left))
        right = max(0, self.dfs(root.right))

        total = root.val + left + right
        self.global_max = max(self.global_max, total)

        return root.val + max(left, right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max = float("-inf")
        self.dfs(root)
        return self.global_max