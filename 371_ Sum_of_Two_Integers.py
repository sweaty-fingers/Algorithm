class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        MASK = 0xFFFFFFFF
        MAX_ = 0x7FFFFFFF
        
        a = bin(a & MASK)[2:].zfill(32)
        b = bin(b & MASK)[2:].zfill(32)
        
        print(a)
        print(b)
        carry = 0
        output = []
        length = 32
        for i in range(length):
            A = int(a[length - i - 1])
            B = int(b[length - i - 1])
            
            Q1 = A & B
            Q2 = A ^ B
            Q3 = Q2 & carry
            sum_ = Q2 ^ carry
            carry = Q1 | Q3
            
            output.append(str(sum_))
            
        output = output[::-1]
        output = int("".join(output), 2)
        print(bin(output)[2:])
        
        if output > MAX_:
            output = ~(output ^ MASK)
            print(bin(output))
            print(output)
        
        return output
