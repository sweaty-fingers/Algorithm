# 팩토리얼 함수를 정의하고 컴비네이션으로 풀이
##
##1. 2step이 하나씩 늘어갈 때 마다 전체 step 수가 줄어듦
##    1. num of  2steps = i
##    2. total steps = n - i
##    3. num of 1step = n - 2i
##2. n 이 짝수일 때 종료 조건과 홀수일 때 종료 조건을 다르게 줌


class Solution:
    def climbStairs(self, n: int) -> int:
        def factorial(num):
            if num <= 1:
                return 1

            return int(factorial(num - 1) * num)

        result = 0
        if n == 1:
            return 1
        for i in range(0, n + 1):
            if i == 0:
                result += 1
                continue
            elif i == n - i and n // 2 == 0:  # n이 짝수일 때 종료 조건
                result += 1
                break

            result += factorial(n - i) / factorial(n - 2 * i) / factorial(i)

            if i == n - i - 1 and n // 2 == 1:  # n이 홀수일 때 종료 조건
                break

        return int(result)


# 타뷸레이션 풀이
##
##1. 피보나치 방법과 유사하게 풀이
##    1. 매 잔여 스탭에서 1과 2로 분할했을 때 나올 수 있는 경우의 수를 누적
##    2. 브루트 포스로 풀 경우 time out 발생
##        1. 타뷸레이션을 통해 한번 계산한 값을 저장해서 계산량을 줄임


class Solution:

    steps = collections.defaultdict(int)

    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        if n == 2:
            return 2

        if self.steps[n]:
            return self.steps[n]

        for i in range(3, n + 1):
            self.steps[i] = self.climbStairs(i - 1) + self.climbStairs(i - 2)

        return self.steps[n]
