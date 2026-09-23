class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map, s_map = {}, {}
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1
        i = 0
        matched = 0

        ans = ""
        min_len = 1001

        for j in range(len(s)):
            s_map[s[j]] = s_map.get(s[j], 0) + 1
            if (s_map[s[j]] == t_map.get(s[j], 0)):
                matched+=1
            
            while(matched==len(t_map)):
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    ans = s[i:j + 1]
                s_map[s[i]] -= 1

                if s_map[s[i]] < t_map.get(s[i], 0):
                    matched -= 1
                i+=1
        return ans
            