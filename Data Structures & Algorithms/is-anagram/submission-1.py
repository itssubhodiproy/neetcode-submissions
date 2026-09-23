class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
        
        for c in t:
            if c in freq and freq[c]>0:
                freq[c] -= 1
            else:
                return False
        return True
            
            