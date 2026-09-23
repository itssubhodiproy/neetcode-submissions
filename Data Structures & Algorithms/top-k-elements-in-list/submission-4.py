class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        freq_arr = [[] for _ in range(len(nums)+1)]

        for key in freq_map:
            freq_arr[freq_map[key]].append(key)
        
        ans = []
        for freq in range(len(freq_arr) - 1, 0, -1):
            for num in freq_arr[freq]:
                ans.append(num)

                if len(ans) == k:
                    return ans

        