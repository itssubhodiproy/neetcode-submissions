class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast_ptr = 0
        slow_ptr = 0
        while(True):
            fast_ptr = nums[nums[fast_ptr]]
            slow_ptr = nums[slow_ptr]
            
            if (fast_ptr==slow_ptr):
                break
        
        fast_ptr = 0

        while(True):
            fast_ptr = nums[fast_ptr]
            slow_ptr = nums[slow_ptr]

            if (fast_ptr==slow_ptr):
                break
        
        return fast_ptr
