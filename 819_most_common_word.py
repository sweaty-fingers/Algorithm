class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        paragraph = paragraph.lower()
        paragraph = re.sub('[^0-9a-z]', " ", paragraph)
        
        word_list = paragraph.split()
        
        word_list = [i for i in word_list if i not in banned]
        
        word_numbs = collections.defaultdict(int)
        
        for word in word_list:
            if word not in word_numbs:
                word_numbs[word] = 1
            else:
                word_numbs[word] += 1
                
        result = sorted(word_numbs.items(), key=lambda x : -x[1])
        
        return result[0][0]