class Solution {
    vector<int> sortThree(int a, int b, int c) {
        if(a > b) swap(a, b);
        if(b > c) swap(b, c);
        if(a > b) swap(a, b);
        return {a, b, c};
    }
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> ansBucket;
        int n = nums.size();
        for(int i=0;i<n-2;i++){
            for (int j=i+1;j<n-1;j++){
                for (int k=j+1;k<n;k++){
                    if (nums[i]+nums[j]+nums[k]==0){
                        vector<int>v = sortThree(nums[i], nums[j], nums[k]);
                        ansBucket.insert(v);
                    }
                }
            }
        }
        vector<vector<int>> returnBucket;
        for(auto it: ansBucket) returnBucket.push_back(it);
        return returnBucket;
    }
};
