class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        mini = r
        while(l<=r):
            m = l+(r-l)//2
            com_hr = 0
            for pile in piles:
                com_hr += (pile + m - 1) // m
            if com_hr <= h:
                mini = min(mini, m)
                r = m-1
            elif com_hr > h:
                l = m+1
        return mini
            
            