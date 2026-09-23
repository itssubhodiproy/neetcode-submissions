class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        map<int, int>m;
        for(int i=0;i<n;i++){
            int reqNum = target-nums[i];
            if(m.count(reqNum)) return {m[reqNum], i};
            m[nums[i]]=i;
        }
        return {};
    }
};
