class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        freq_arr = [[] for _ in range(len(nums)+1)]

        for key in freq_map.keys():
            freq_arr[freq_map[key]].append(key)
        
        # gather your ans:
        freq_arr.reverse()
        i = 0
        ans = []
        while(i != k):
            for arr in freq_arr:
                if i==k:
                    break
                for num in arr:
                    if i==k:
                        break
                    ans.append(num)
                    i += 1
        return ans

        