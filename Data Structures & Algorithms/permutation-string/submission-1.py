class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0] * 26
        s2_count = [0] * 26

        for c in s1:
            s1_count[ord(c) - ord('a')] += 1

        i = 0

        for j in range(len(s2)):
            idx = ord(s2[j]) - ord('a')
            s2_count[idx] += 1

            while s2_count[idx] > s1_count[idx]:
                left_idx = ord(s2[i]) - ord('a')
                s2_count[left_idx] -= 1
                i += 1

            if j - i + 1 == len(s1):
                return True

        return False