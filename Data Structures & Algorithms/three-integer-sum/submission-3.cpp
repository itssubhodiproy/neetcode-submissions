class Solution {
    vector<int> sortThree(int a, int b, int c) {
        if(a > b) swap(a, b);
        if(b > c) swap(b, c);
        if(a > b) swap(a, b);
        return {a, b, c};
    }
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> ansBucket; unordered_set<int>s;
        int n = nums.size();
        for(int i=0;i<n-1;i++){
            for (int j=i+1;j<n;j++){
                if(s.count(-(nums[i]+nums[j]))) {
                    vector<int>v = sortThree(nums[i], nums[j], -(nums[i]+nums[j]));
                    ansBucket.insert(v);
                }
                s.insert(nums[j]);
            }
            s.clear();
        }
        vector<vector<int>> returnBucket;
        for(auto it: ansBucket) returnBucket.push_back(it);
        return returnBucket;
    }
};
