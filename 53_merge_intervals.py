class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        
        output = []
        temp = intervals[0]
        
        for now in intervals:
            if now[0] <= temp[1]:
                if now[1] < temp[1]:
                    continue
                temp = [temp[0], now[1]]
                continue
            
            
            output.append(temp)
            temp = now
            print(output)

            
        output.append(temp)
        print(output)
        
        return output