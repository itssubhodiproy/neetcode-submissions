class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(left, right, strs):
            if right==0 and left==0:
                ans.append(strs)
                return
            if left>0:
                strs+="("
                backtrack(left-1, right, strs)
                strs = strs[:-1] 
            if right > left:
                strs+=")"
                backtrack(left, right-1, strs)
                strs = strs[:-1] 
        
        backtrack(n, n, "")
        return ans