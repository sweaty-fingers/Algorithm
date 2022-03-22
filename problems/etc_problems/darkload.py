# 이코테 책 그래프 문제, 어두운 길
# 크루스칼 알고리즘 이용, (전체 길의 비용 - 최소 신장트리의 총 비용)을 구하면 된다. 

def get_input():
    n, m = map(int, input().split(" "))
    
    graph = []
    for _ in range(m):
        x, y, cost = list(map(int, input().split(" ")))
        graph.append((cost, x, y))
    
    return n, m, graph


def union_parent(parent, x, y):
    x = parent[x]
    y = parent[y]

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]


def kruskal(graph, n, m):

    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i

    graph.sort()
    cost_total = 0
    cost_result = 0

    for g in graph:
        cost, x, y = g
        cost_total += cost

        if find_parent(parent, x) != find_parent(parent, y):
            union_parent(parent, x, y)
            cost_result += cost
    
    return cost_total - cost_result


def main():
    n, m, graph = get_input()

    print(kruskal(graph, n, m))

if __name__ == "__main__":
    main()