class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int i=0, j=0, n=s.size(), ans=0;
        map<char, int>m;
        while(j<n){
            m[s[j]]++;
            int winLen = j-i+1;
            if(m.size()==winLen){
                ans=max(ans, winLen);
            } else {
                m[s[i]]--;
                if(m[s[i]]==0) m.erase(s[i]);
                i++;
            }
            j++;
        }
        return ans;
    }
};
