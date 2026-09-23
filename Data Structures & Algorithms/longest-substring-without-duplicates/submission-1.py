class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        max_len = 0
        bucket = set()
        for j in range(len(s)):
            while(s[j] in bucket):
                bucket.remove(s[i])
                i+=1
            bucket.add(s[j])
            max_len = max(max_len, j-i+1)
        return max_len
