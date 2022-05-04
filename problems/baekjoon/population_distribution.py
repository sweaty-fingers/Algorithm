# https://www.acmicpc.net/problem/16234
# 인구 이동
from collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# import logging

# simple_formatter = logging.Formatter("[%(name)s] %(message)s")
# console_handler = logging.StreamHandler()
# console_handler.setFormatter(simple_formatter)
# console_handler.setLevel(logging.INFO)

# root_logger = logging.getLogger(__name__)
# root_logger.addHandler(console_handler)
# root_logger.setLevel(logging.INFO)


def get_input():
    global L, R
    N, L, R = map(int, input().split(" "))
    
    graph = [list(map(int, input().split(" "))) for _ in range(N)]
    
    return graph


def dfs(graph):
    
    n = len(graph)
    m = len(graph[0])
    
    
    day = 0
    
    while day < 2000:
        seen = []
        is_move = False
        groups = []
        groups_sum = []
        index = 0
        for i in range(n):
            for j in range(m):
                if (i, j) in seen:
                    # root_logger.info(f"seen: {seen}")
                    continue
                
                seen.append((i, j))
                q = deque([])
                _sum = graph[i][j]
                group = [(i, j)]
                q.append((graph[i][j], i, j))
                index += 1
                
                while q:
                    value, y, x = q.popleft()
                
                    for dy, dx in move:
                        y_tmp, x_tmp = y + dy, x + dx
                        
                        if (y_tmp, x_tmp) in seen:
                            continue
                    
                        if not ((0 <= y_tmp < n) and (0 <= x_tmp < m)):
                            continue
                    
                        if L <= abs(value - graph[y_tmp][x_tmp]) <= R:
                            is_move = True
                            _sum += graph[y_tmp][x_tmp]
                            group.append((y_tmp, x_tmp))
                            seen.append((y_tmp, x_tmp))
                            q.append((graph[y_tmp][x_tmp], y_tmp, x_tmp))
                            index += 1
                
                
                if len(group) > 1:
                    # print(groups)
                    groups.append(group)
                    groups_sum.append(_sum // len(group))
                    
                group = []
                _sum = 0
                    
        if is_move:
            # print(f"groups: {groups}")
            for i, group in enumerate(groups):
                for (y, x) in group:
                    graph[y][x] = groups_sum[i]
                    
        
            day += 1
        else:
            return graph, day
    
    return graph, day


def main():
    graph = get_input()
    
    # root_logger.info("previous graph")
    # for g in graph:
    #     root_logger.info(g)
    
    graph, day = dfs(graph)
    # root_logger.info("graph after")
    # for g in graph:
    #     root_logger.info(g)
        
    print(day)
    
if __name__ == "__main__":
    main()