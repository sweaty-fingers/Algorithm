def get_input():
    n, m = map(int, input().split(" "))

    loads = []
    for _ in range(m):
        loads.append(tuple(map(int, input().split(" "))))
    
    return n, loads


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
    n, loads = get_input()
    loads = sorted(loads, key=lambda x: x[-1])
    costs = []

    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i

    for load in loads:
        a, b, cost = load
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            costs.append(cost)

    print(sum(costs[:-1]))

if __name__ == "__main__":
    main()