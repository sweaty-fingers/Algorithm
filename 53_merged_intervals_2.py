class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
            
        output = []
        
        for i in sorted(intervals, key=lambda x: x[0]):
            if output and i[0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], i[1])
            else:
                output.append(i)
            
        return output`