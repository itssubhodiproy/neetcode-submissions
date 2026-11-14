class Solution:
    def carFleet(self, finish: int, start: List[int], pace: List[int]) -> int:
        
        if len(start) == 1:
            return 1
        
        k_pace = {}
        for i in range(len(pace)):
            k_pace[start[i]] = pace[i]
        
        start.sort(reverse=True)
        count = 0
        prev_time = 0

        for i in range(len(start)):
            result = (finish - start[i]) / k_pace[start[i]]
            if result > prev_time:
                count += 1
                prev_time = result 
        return count

