class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map, s2_map = {}, {}

        for c in s1:
            s1_map[c] = s1_map.get(c, 0) + 1
        
        i = 0

        for j in range(len(s2)):
            s2_map[s2[j]] = s2_map.get(s2[j],0)+1

            while(s2_map.get(s2[j],0) > s1_map.get(s2[j], 0)):
                s2_map[s2[i]] -= 1
                if s2_map[s2[i]] == 0:
                    del s2_map[s2[i]]
                i+=1
            if (j-i+1 == len(s1)):
                return True
            
        return False