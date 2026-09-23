class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans, n = 0, len(s)
        for i in range(n):
            freq_map, maxF = {}, 0
            for j in range(i, n):
                freq_map[s[j]] = 1+freq_map.get(s[j], 0)
                maxF = max(maxF, freq_map[s[j]])
                if (j-i+1)- maxF <= k:
                    ans = max(j-i+1, ans)
        return ans
