from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace(",", " ")
        paragraph = paragraph.lower()
        paragraph = paragraph.split()
        
        para = []
        for p in paragraph:
            words = ""
            for w in p:
                if w.isalpha():
                    words += w
            para.append(words)
            
        counts = Counter(para)
        for b in banned:
            counts[b] = 0
        
        
        return counts.most_common(1)[0][0]
        