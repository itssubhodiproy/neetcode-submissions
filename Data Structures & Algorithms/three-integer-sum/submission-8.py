class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
    
        ans = []
        for i in range(0, n - 2): # Optimized bound to n-2 since we need 3 elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            bucket = set()
            j = i + 1
            while j < n:
                complement = -(nums[i] + nums[j])
                if complement in bucket:
                    ans.append([nums[i], complement, nums[j]]) # Append in sorted order
                    
                    # Skip duplicate values for the third element (nums[j])
                    while j + 1 < n and nums[j] == nums[j + 1]:
                        j += 1
                        
                bucket.add(nums[j])
                j += 1

        return ans