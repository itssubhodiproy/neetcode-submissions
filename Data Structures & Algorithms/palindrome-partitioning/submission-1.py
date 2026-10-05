class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def is_palindrome(strs: str) -> bool:
            return strs == strs[::-1]

        def backtrack(arr, i):
            if i == len(s):
                if is_palindrome(arr[-1]):
                    ans.append(arr.copy())
                return

            # DON'T CUT
            arr[-1] += s[i]
            backtrack(arr, i + 1)
            arr[-1] = arr[-1][:-1]

            # CUT
            if is_palindrome(arr[-1]):
                arr.append(s[i])
                backtrack(arr, i + 1)
                arr.pop()

        backtrack([s[0]], 1)
        return ans