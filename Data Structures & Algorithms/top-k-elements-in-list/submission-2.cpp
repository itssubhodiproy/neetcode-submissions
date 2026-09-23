class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int>bucket;
        priority_queue<pair<int, int>>max_pq;
        vector<int> ans;
        for(auto it: nums) bucket[it]++;
        for(auto it: bucket) max_pq.push({it.second, it.first});
        for (int i=0;i<k;i++) {
            ans.push_back(max_pq.top().second);
            max_pq.pop();
        }
        return ans;
    }
};
