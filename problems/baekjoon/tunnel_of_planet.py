# 백준 위성터널 문제
# https://www.acmicpc.net/problem/2887
# x, y, z 마다 개별적으로 최소 신장 트리를 만든 후 graph에 넣어서 kruskal 알고리즘을 수행한다.
def get_input():
    n = int(input())

    xs = []
    ys = []
    zs = []
    for i in range(1, n + 1):
        x, y, z = tuple(map(int, input().split(" ")))
        xs.append((x, i)) 
        ys.append((y, i))
        zs.append((z, i))

    xs.sort()
    ys.sort()
    zs.sort()

    graph = []
    for i in range(n - 1):
        cost_x_a, x_a = xs[i]
        cost_x_b, x_b = xs[i + 1]
        cost_y_a, y_a = ys[i]
        cost_y_b, y_b = ys[i + 1]
        cost_z_a, z_a = zs[i]
        cost_z_b, z_b = zs[i + 1]

        graph.append((cost_x_b - cost_x_a, x_a, x_b))
        graph.append((cost_y_b - cost_y_a, y_a, y_b))
        graph.append((cost_z_b - cost_z_a, z_a, z_b))
        
    return n, graph

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]


def kruskal(graph, n):
    parent = [0] * (n + 1)
    
    for i in range(1, n + 1):
        parent[i] = i
    
    graph.sort()
    cost_total = 0

    for g in graph:
        cost, x, y = g

        if find_parent(parent, x) != find_parent(parent, y):
            union_parent(parent, x, y)
            cost_total += cost
    
    return cost_total


def main():
    n, graph = get_input()
    
    print(kruskal(graph, n))

if __name__ == "__main__":
    main()