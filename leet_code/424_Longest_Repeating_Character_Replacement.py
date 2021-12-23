class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = collections.Counter()
        max_len = 0
        
        for right in range(len(s)):
            
            count[s[right]] += 1
            n_max_char = count.most_common(1)[0][1]
            
            if right - left + 1 - n_max_char > k:
                count[s[left]] -= 1
                left += 1
                
            max_len = max(right-left + 1, max_len)
            
        return max_len
            