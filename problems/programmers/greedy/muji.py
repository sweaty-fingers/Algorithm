# 프로그래머스 무지의 먹방 라이브
# https://programmers.co.kr/learn/courses/30/lessons/42891 
import heapq

def solution(food_times, k):
    answer = 0

    if sum(food_times) <= k:
        return -1

    q_food = []
    for i, f in enumerate(food_times):
        heapq.heappush(q_food, (f, i + 1))

    prev = 0
    len_ = len(q_food)
    while len_ * (q_food[0][0] - prev) <= k:

        f, i = heapq.heappop(q_food)
        r = f - prev

        k -= len_ * r
        prev = f
        len_ = len(q_food)

    if not q_food:
        return -1

    q_food = sorted(q_food, key=lambda x: x[1])

    return q_food[k % len_][1]
