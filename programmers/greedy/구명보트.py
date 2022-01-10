# 실행시간 초과
from bisect import bisect_right


def solution(people, limit):

    if len(people) == 1:
        return 1

    answer = 0

    people.sort()

    while people:
        p = people.pop()
        limit_temp = limit - p

        idx = bisect_right(people, limit_temp)
        if idx > 0:
            p = people.pop(idx - 1)
            answer += 1
            continue

        answer += 1

    return answer


## 통과
from bisect import bisect_right
from collections import deque


def solution(people, limit):

    answer = 0
    people.sort()
    people = deque(people)

    while people:
        limit_temp = limit - people.pop()

        if people and limit_temp >= people[0]:
            people.popleft()

        answer += 1
    return answer
