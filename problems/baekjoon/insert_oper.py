# https://www.acmicpc.net/problem/14888

import logging
from collections import deque

simple_formatter = logging.Formatter("[%(name)s] %(message)s")
console_handler = logging.StreamHandler()
console_handler.setFormatter(simple_formatter)
console_handler.setLevel(logging.INFO)

root_logger = logging.getLogger(__name__)
root_logger.addHandler(console_handler)
root_logger.setLevel(logging.WARNING)


def get_input():
    N = int(input())
    total_nums = list(map(int, input().split(" ")))
    total_opers = list(map(int, input().split(" ")))
    
    return total_nums, total_opers


def bfs(total_nums, total_opers):
    count = 0
    q = deque([])
    q.append((total_nums[count], count + 1, total_opers[:]))
    results = []
    while q:
        root_logger.info(q)
        value_cur, count, remain_opers = q.popleft()

        if sum(remain_opers) == 0:
            results.append(value_cur)
            continue
         
        for i in range(4):
            value_next = value_cur
            if remain_opers[i] == 0:
                continue
            
            if i == 0:
                value_next += total_nums[count]
            elif i == 1:
                value_next -= total_nums[count]
            elif i == 2:
                value_next *= total_nums[count]
            else:
                if value_next < 0:
                    value_next = ((-1 * value_next) // total_nums[count]) * -1
                else:
                    value_next //= total_nums[count]
                    
            next_opers = remain_opers[:]
            next_opers[i] -= 1
            q.append((value_next, count + 1, next_opers))
    
    return results    
            
def main():
    total_nums, total_opers = get_input()
    
    root_logger.info(f"total_nums: {total_nums}")
    root_logger.info(f"total_opers: {total_opers}")
    
    results = bfs(total_nums, total_opers)
    print(max(results))
    print(min(results))

if __name__ == "__main__":
    main()