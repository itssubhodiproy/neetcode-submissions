class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for single_string in strs:
            encoded_str += f"{len(single_string)}#{single_string}"
        return encoded_str
    def decode(self, s: str) -> List[str]:
        ans = []
        i=0
        while(i < len(s)):
            dig = ""
            while s[i]!='#':
                dig += s[i]
                i += 1
            i+=1
            prob_str = ""
            digit = int(dig)
            while(digit):
                prob_str += s[i]
                digit -= 1
                i += 1
            ans.append(prob_str)
        return ans