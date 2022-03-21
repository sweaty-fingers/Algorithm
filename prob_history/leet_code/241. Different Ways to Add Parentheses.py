class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left, right, op):

            results = []

            for l in left:
                for r in right:
                    # eval을 이용하여 문자열을 표현식으로 바꿈
                    results.append(eval(f"{l}{op}{r}"))

            return results

        # 재귀문 처음 반환 조건 : 단일 숫자일 때
        # 처음 반환 조건이 없으면 빈 리스트만 출력됨
        if expression.isdigit():
            return [int(expression)]

        results = []

        for index, op in enumerate(expression):

            if op in "-*+":
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index + 1 :])

                # extend를 이용해서 리스트 차원을 유지한 채 병합 (append와 차이)
                results.extend(compute(left, right, op))

        return results
