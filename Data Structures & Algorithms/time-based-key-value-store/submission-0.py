class TimeMap:

    def __init__(self):
        self.my_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.my_map:
            self.my_map[key].append((timestamp, value))
        else:
            self.my_map[key] = [(timestamp, value)]   

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.my_map: return ""
        l, r=0, len(self.my_map[key])-1
        ans = ""
        while(l<=r):
            m = l+(r-l)//2
            if self.my_map[key][m][0]==timestamp:
                return self.my_map[key][m][1]
            elif self.my_map[key][m][0]<timestamp:
                ans = self.my_map[key][m][1]
                l = m+1
            else:
                r = m-1
        return ans
            
                

        
