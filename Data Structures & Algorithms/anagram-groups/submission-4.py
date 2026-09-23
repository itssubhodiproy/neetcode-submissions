class Solution:
    def canonical(self, string: str) -> str:
        # create a freq map & then create a string from there which will be our key
        freq_map = {}
        ans_str = ""
        for c in string:
            if c in freq_map:
                freq_map[c] += 1
            else: 
                freq_map[c] = 1
        for key in sorted(freq_map):
            ans_str+=f"{key}-{freq_map[key]}"
        return ans_str
        # iterate over map and create a str from the map
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