# 크루스칼 알고리즘을 이용한 최소 신장트리

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    

def main():
    n = 7

    # [node_a, node_b, cost]: node_a -> node_b for cost
    graph = [[1, 2, 3], [1, 3, 2], [3, 2, 1], [2, 5, 2], [3, 4, 4], [7, 3, 6], [5, 1, 5], [1, 6, 2], [6, 4, 1], [6, 5, 3], [4, 5, 3], [6, 7, 4]] 
    
    # 비용을 기준으로 오름차순 정렬 (낮은 cost가 앞으로)
    graph = sorted(graph, key=lambda x: x[-1]) 
    
    cost_total = 0

    # 부모 노드 자기 자신으로 초기화
    parent = [0] * (n + 1)

    for i in range(1, n + 1):
        parent[i] = i

    for load in graph:
        a, b, cost = load

        # 사이클이 발생하지 않을 경우 유니온 연산 (루트 노드가 같아질 경우 사이클이 발생한 것.)
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            cost_total += cost

    print(cost_total)


if __name__ == "__main__":
    main()

# 출력 값
# 12