class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<vector<int>, vector<string>> m;
        int n = strs.size();

        for(int i=0;i<n;i++){
            vector<int>v(26,0);
            string currString = strs[i];
            for(int j=0;j<currString.size();j++){
                int ind = currString[j]-'a';
                v[ind]++;
            }
            m[v].push_back(currString);
        }

        // take out everything from map, put it into vector and return
        vector<vector<string>> ans;
        for(auto i: m) ans.push_back(i.second);
        return ans;
    }
};
