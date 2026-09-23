class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)
        maxi = 0
        for num in seen:
            if num-1 not in seen:
                number = num
                count = 1
                while number + 1 in seen:
                    if number+1 in seen:
                        count+=1
                        number+=1
                    else:
                        break
                maxi=max(maxi, count)
        return maxi