class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []
        
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        nums, ans = [], []

        for digit in digits:
            nums.append(mapping[digit])
        
        def backtrack(i, curr_str):
            if i == len(nums):
                ans.append(curr_str)
                return 
            
            for char in nums[i]:
                backtrack(i+1, curr_str+char)
        
        backtrack(0, "")
        return ans