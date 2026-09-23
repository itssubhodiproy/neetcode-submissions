class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<map<char, int>, vector<string>> m;
        int n = strs.size();

        for(int i=0;i<n;i++){ // O(n)
            map<char, int>mp;
            string currString = strs[i];
            for(int j=0;j<currString.size();j++){ // O(n)
                mp[currString[j]]++;
            }
            m[mp].push_back(currString);
        }

        // Total O(n2)

        // take out everything from map, put it into vector and return
        vector<vector<string>> ans;
        for(auto i: m) ans.push_back(i.second);
        return ans;
    }
};
