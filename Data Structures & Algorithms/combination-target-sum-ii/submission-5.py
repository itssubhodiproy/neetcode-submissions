class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def backtrack(i, arr, total):
            if total == target:
                ans.append(arr.copy())
                return
            if i == len(candidates) or total > target:
                return
            # pick candidates
            arr.append(candidates[i])
            backtrack(i+1, arr, total+candidates[i])
            arr.pop()
            # don't pick and skip all ele idential to curr ele 
            # (they will appear adjacently coz they're sorted)
            j = i+1
            while(j<len(candidates) and candidates[i]==candidates[j]):
                j = j+1
            backtrack(j, arr, total)
    
        backtrack(0, [], 0)
        return ans
                