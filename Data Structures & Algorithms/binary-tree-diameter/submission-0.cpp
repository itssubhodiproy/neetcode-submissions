/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int res = 0;
        int maxLen = func(root, res);
        return res;
    }
    int func(TreeNode* root, int &res){
        if(!root) return 0;
        int leftHeight = func(root->left, res);
        int rightHeight = func(root->right, res);
        res = max(res, leftHeight+rightHeight);
        return 1+max(leftHeight, rightHeight);
    }
};
