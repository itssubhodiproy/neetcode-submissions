class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair_arr = []

        for i in range(len(position)):
            tuple_pair = (position[i], speed[i])
            pair_arr.append(tuple_pair)

        pair_arr.sort()

        stack = []

        for i in range(len(pair_arr) - 1, -1, -1):
            curr_time = (target - pair_arr[i][0]) / pair_arr[i][1]

            if(stack and curr_time <= stack[-1]):
                continue
            
            stack.append(curr_time)

        return len(stack)