class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def backtrack(start, arr, target):
            if target == 0:
                ans.append(arr.copy())
                return
            if target < 0:
                return
            prev = -1
            for i in range(start, len(candidates)):
                if prev == candidates[i]:
                    continue
                arr.append(candidates[i])
                backtrack(i+1, arr, target-candidates[i])
                arr.pop()
                prev = candidates[i]
        
        backtrack(0, [], target)
        return ans
                