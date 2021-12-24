class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Parameters
        -----------
        counter : dict {task: str : count: int}
        작업과 횟수 dict

        correction : int
        result 보정 값, 작업 사이에 들어갈 idle 수 결정

        result : 최종 답
        """

        counter = collections.Counter(tasks)

        result = 0
        while True:

            correction = 0
            for i, _ in counter.most_common(n + 1):

                result += 1
                correction += 1

                counter.subtract(i)

                # 0 이하 요소 삭제
                counter += collections.Counter()

            if not counter:
                break

            result += n + 1 - correction

        return result
