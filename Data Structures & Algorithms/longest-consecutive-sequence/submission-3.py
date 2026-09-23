class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # put all nums val at set
        seen = set()
        # traverse arr - and check if left neighbour not exists - start counting the seq? check for LCS
        for num in nums:
            seen.add(num)
        maxi = 0
        for num in nums:
            if num-1 not in seen:
                number = num
                count = 1
                while(True):
                    if number+1 in seen:
                        count+=1
                        number+=1
                    else:
                        break
                maxi=max(maxi, count)
        return maxi