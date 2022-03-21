class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        
        def check(length):
            
            for i in range(length - 1):
                if (start + i + 1) >= len(data) or (data[start + i + 1] >> 6) != 0b10:
                    return False
            
            return True
        
        start = 0 
        while start < len(data):
            
            if (data[start] >> 3) == 0b11110 and check(4):
                start += 4
            elif (data[start] >> 4) == 0b1110 and check(3):
                start += 3
            elif (data[start] >> 5) == 0b110 and check(2):
                start += 2
            elif (data[start] >> 7) == 0b0:
                start += 1
            else:
                return False
            
        return True
            