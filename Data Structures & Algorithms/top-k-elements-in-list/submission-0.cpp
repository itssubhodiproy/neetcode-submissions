class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int>m;
        vector<pair<int, int>>v;
        vector<int>ans;
        for(auto it: nums) m[it]++;
        for(auto it: m) v.push_back(make_pair(it.second, it.first));
        // sort(v.begin(), v.end(), greater<int>());
        sort(v.begin(), v.end(), [](pair<int, int>& a, pair<int, int>& b) {return a.first > b.first;});

        for(int i=0;i<k;i++){
            ans.push_back(v[i].second);
        }
        return ans;
    }
};
