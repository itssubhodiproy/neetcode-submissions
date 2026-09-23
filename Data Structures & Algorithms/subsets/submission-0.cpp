class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> subsets;
        int i=0;
        dfs(ans, subsets, i, nums);
        return ans;
    }
    void dfs(vector<vector<int>> &ans, vector<int> subsets, int i, vector<int> nums){
        if(i==nums.size()) {
            ans.push_back(subsets);
            return;
        }
        subsets.push_back(nums[i]);
        dfs(ans, subsets, i+1, nums);
        subsets.pop_back();
        dfs(ans, subsets, i+1, nums);
    }
};
