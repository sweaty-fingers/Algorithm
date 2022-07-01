from collections import defaultdict
from typing import List

def empty_list():
    return []

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if not strs:
            return [[" "]]
        
        di = defaultdict(empty_list)
        for s in strs:
            s_sort = "".join(sorted(s))
            di[s_sort].append(s)
        
        result = []
        
        for i in di.keys():
            result.append(di[i])
            
        return result