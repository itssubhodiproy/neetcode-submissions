class Solution {
public:
    int maxArea(vector<int>& heights) {
        int n = heights.size(), vol = 0;
        for(int i=0;i<n-1;i++){
            for (int j=i+1;j<n;j++){
                int mini = min(heights[i], heights[j]);
                vol = max(mini*(j-i), vol);
            }
        }
        return vol;
    }
};
