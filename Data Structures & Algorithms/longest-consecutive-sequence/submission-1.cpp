class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size()==0) return 0;
        sort(nums.begin(), nums.end());
        int maxCounter = 1;
        int n = nums.size();
        for(int i=0;i<n-1;i++){
            int counter = 1;
            int currNum = nums[i];
            for(int j = i+1;j<n;j++){
                if(currNum+1==nums[j]){
                    counter++;
                    currNum = nums[j];
                }
            }
            maxCounter=max(maxCounter,counter);
        }
        return maxCounter;
    }
};
