class Solution:
    def canonical(self, string: str) -> str:
        # create a freq arr & then create a string from there which will be our key
        freq_arr = [0]*26
        ans_str = ""
        for c in string:
            freq_arr[ord(c) - ord('a')] += 1
        for i in range(26):
            ans_str+=f"{i}-{freq_arr[i]}"
        return ans_str
        # charfreq-charfreq-charfreq
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for s in strs:
            cano_str = self.canonical(s)
            if cano_str in anagram_map:
                anagram_map[cano_str].append(s)
            else:
                anagram_map[cano_str]=[s]
        ans = []

        for k in anagram_map.keys():
            ans.append(anagram_map[k])
        return ans