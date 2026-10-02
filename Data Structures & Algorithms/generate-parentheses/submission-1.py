class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(left, right, strs):
            if right==0 and left==0:
                ans.append(strs)
                return
            if left > 0:
                backtrack(left-1, right, strs+"(")
            if right > left:
                backtrack(left, right-1, strs+")")
        
        backtrack(n, n, "")
        return ans