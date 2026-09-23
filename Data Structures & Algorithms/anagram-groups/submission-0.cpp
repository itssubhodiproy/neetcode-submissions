class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> m;
        int n = strs.size();

        for(int i=0;i<n;i++){
            string nonSortedString = strs[i];
            string sortedString = strs[i];
            sort(sortedString.begin(), sortedString.end());
            m[sortedString].push_back(nonSortedString);
        }

        // take out everything from map, put it into vector and return
        vector<vector<string>> ans;
        for(auto i: m) ans.push_back(i.second);
        return ans;
    }
};
