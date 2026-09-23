class Solution {
public:
    int maxArea(vector<int>& heights) {
        int n = heights.size(), vol=0;
        int i=0,j=n-1;
        while(i!=j){
            vol = max(vol, min(heights[i], heights[j])*(j-i));
            heights[i]<heights[j]?i++:j--;
        }
        return vol;
    }
};
