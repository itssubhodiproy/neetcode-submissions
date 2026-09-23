class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<int>subsets;
        vector<vector<int>>ans;
        dfs(nums, 0, target, subsets, ans);
        return ans;
    }
    void dfs(vector<int>nums, int i, int target, vector<int>subsets, vector<vector<int>>&ans){
        if(i<nums.size() && target==0) {
            ans.push_back(subsets);
            return;
        }
        if(i==nums.size()||target<0) return;
        subsets.push_back(nums[i]);
        dfs(nums, i, target-nums[i], subsets, ans);
        subsets.pop_back();
        dfs(nums, i+1, target, subsets, ans);
    }
};