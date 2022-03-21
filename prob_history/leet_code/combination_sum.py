class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        
        results = []
        results_temp = []
        
        def dfs(elements, k):
            
            if k == 0:
                results.append(results_temp[:])
            
            for e in elements:
                
                if not results_temp:
                    results_temp.append(e)
                    dfs(elements, k - e)
                    results_temp.pop()
                    
                elif (e <= k and e <= results_temp[-1]):
                    results_temp.append(e)
                    dfs(elements, k - e)
                    results_temp.pop()
                    
        candidates.sort(reverse=True)
        dfs(candidates, target)
        
        return results
                    