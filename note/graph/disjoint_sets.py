# 서로소 집합

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

def main():
    n = 5 # 노드 개수
    graph = [[3, 2], [4, 2], [1, 2]]  
    parent = [0] * (n + 1)

    # 자기 자신으로 초기화
    for i in range(1, n + 1):
        parent[i] = i

    for g in graph:
        a, b = g

        #if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)

    for i in range(1, n + 1):
        print(find_parent(parent, i), end=' ')

if __name__ == "__main__":
    main()

# 출력 값
# 1 1 1 1 5