class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int>m;
        priority_queue <pair<int, int>>pq;
        vector<int>ans;
        for(auto it: nums) m[it]++;
        for(auto it: m) pq.push(make_pair(it.second, it.first));
    
        for(int i=0;i<k;i++){
            ans.push_back(pq.top().second);
            pq.pop();
        }
        return ans;
    }
};
