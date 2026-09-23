class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int>s;
        int n = nums.size();
        for (int num : nums){
            if(s.count(num)) return true;
            s.insert(num);
        }
        return false;
    }
};