class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int>v(26, 0);
        int i=0, j=0, n=s.size(), ans=0;
        while(j<n){
            v[s[j]-'A']++;
            int max_ele = *max_element(v.begin(), v.end());
            int win_length = j-i+1;
            if(win_length-max_ele<=k)
                ans=max(ans, win_length);
            else{
                v[s[i]-'A']--;
                i++;
            }
            j++;
        }
        return ans;
    }
};
