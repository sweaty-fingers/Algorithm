class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        results = []
        results_tmp = []
        
        def dfs(elements, start):
            
            results.append(results_tmp[:])
                
            for i in range(start, len(elements)):
                results_tmp.append(elements[i])
                dfs(elements, i+1)
                results_tmp.pop()
                
        
        dfs(nums, 0)
        
        return results
        