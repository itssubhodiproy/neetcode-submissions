class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int>prefix(n), postfix(n), ans(n);
        // prefix array creation
        prefix[0] = nums[0];
        for(int i=1;i<n;i++){
            prefix[i] = prefix[i-1]*nums[i];
        }
        // prefix array creation
        postfix[n-1] = nums[n-1];
        for(int i=n-2;i>=0;i--){
            postfix[i] = postfix[i+1]*nums[i];
        }
        // ans array creation
        for(int i=0;i<n;i++){
            if(i==0) ans[i] = postfix[i+1];
            else if(i==n-1) ans[i] = prefix[i-1];
            else ans[i] = postfix[i+1]*prefix[i-1];
        }
        return ans;
    }
};
