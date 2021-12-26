# 하향식 다이나믹 프로그래밍
# 하위문제를 계산했는지 확인해가며  풀이, 계산한 값을 저장, 한번 계산한 값은 딕셔너리에 저장,  다시 계산할 필요 x
class Solution:
    
    F = collections.defaultdict(int) # default dict,
    
    def fib(self, n: int) -> int:
        
        if n <= 1:
            return n # (f(0) 과 f(1)에 대한 처리)
       
        if self.F[n]:
            return self.F[n] # 값이 존재하면 계산 불러오기 (계산 시간을 줄임)
        
        self.F[n] = self.fib(n-1) + self.fib(n-2) # 값 계산, 저장
        
        return self.F[n]



# 상향식 다이나믹 프로그래밍
# 아래서부터 계산, 계산한 값을 저장
class Solution:
    
    def fib(self, n: int) -> int:
        F = collections.defaultdict(int)
        
        F[0] = 0
        F[1] = 1
        
        for i in range(2, n + 1):
            F[i] = F[i - 1] + F[i - 2]
        
        return F[n]