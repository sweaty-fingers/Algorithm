# 이코테 그래프 이론 문제: 여행 계획

def get_input():
    n, m = map(int, input().split(" "))
    
    graph = [[0] for _ in range(n + 1)]

    for _ in range(1, n + 1):
        graph[_] += list(map(int, input().split(" ")))

    plan = list(map(int, input().split(" ")))

    return n, m, graph, plan

def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)

    if a < b:
        parents[b] = a

def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def main():
    n, m, graph, plan = get_input()
    print(f"n: {n}, m: {m}, graph: {graph}, plan: {plan}")

    parents = [0] * (n + 1)

    for i in range(1, n + 1):
        parents[i] = i

    for i in range(1, n + 1):
        b = - 1

        while True:
            if graph[i][b + 1:].count(1) == 0 or b == n:
                break

            b += graph[i][b + 1:].index(1) + 1
            print(f"b: {b}")
            print(find_parent(parents, i), find_parent(parents, b))
            if find_parent(parents, i) != find_parent(parents, b):
                union_parent(parents, i, b)
                print(find_parent(parents, i), find_parent(parents, b))
                print(" ")

    for i in range(len(plan)):
        if i == 0:
            prev = find_parent(parents, plan[i])
            continue
        cur = find_parent(parents, plan[i])
        if cur != prev: 
            return print("NO")
    
    return print("YES")
        
if __name__ == "__main__":
    main()