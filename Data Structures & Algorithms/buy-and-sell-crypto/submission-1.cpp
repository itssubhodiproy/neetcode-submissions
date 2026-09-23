class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int mini = 101, maxi = -1, n=prices.size();
        for(int i=0;i<n;i++){
            mini = min(mini, prices[i]);
            maxi = max(maxi, prices[i]-mini);
        }
        return maxi;
    }
};
