def get_input():
    n, m = map(int, input().split(" "))
    
    graph = []
    for _ in range(m):
        x, y, cost = map(int, input().split(" "))
        graph.append((cost, x, y))
        
    return graph, n


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
    graph, n = get_input()
    
    graph.sort()
    
    parent = [i for i in range(n + 1)]
    
    final_cost = 0
    total_cost = 0
    for g in graph:
        cost, a, b = g
        total_cost += cost
        if find_parent(parent, a) == find_parent(parent, b):
            continue
        
        final_cost += cost
        union_parent(parent, a, b)
        
    print(total_cost - final_cost)
            

if __name__ == "__main__":
    main()
    
# 7 11
# 0 1 7
# 0 3 5
# 1 2 8
# 1 3 9
# 1 4 7
# 2 4 5
# 3 4 15
# 3 5 6
# 4 5 8
# 4 6 9
# 5 6 11

# output
# 51