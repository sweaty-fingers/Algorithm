# https://www.acmicpc.net/problem/2887
# 백준 행성터널

def get_input():
    n = int(input())
    
    node_x = [] 
    node_y = []
    node_z = []
    
    for i in range(1, n + 1):
        x, y, z = map(int, input().split(" "))
        node_x.append((x, i))
        node_y.append((y, i))
        node_z.append((z, i))
    
    node_x.sort()
    node_y.sort()
    node_z.sort()

    graph = []
    
    for i in range(n - 1):
        x_prev, node_x_prev = node_x[i]
        x_next, node_x_next = node_x[i + 1]
        y_prev, node_y_prev = node_y[i]
        y_next, node_y_next = node_y[i + 1]
        z_prev, node_z_prev = node_z[i]
        z_next, node_z_next = node_z[i + 1]
        
        graph.append((node_x_prev, node_x_next, abs(x_next - x_prev)))
        graph.append((node_x_next, node_x_prev, abs(x_next - x_prev)))
        graph.append((node_y_prev, node_y_next, abs(y_next - y_prev)))
        graph.append((node_y_next, node_y_prev, abs(y_next - y_prev)))
        graph.append((node_z_prev, node_z_next, abs(z_next - z_prev)))
        graph.append((node_z_next, node_z_prev, abs(z_next - z_prev)))
    
    graph = sorted(graph, key=lambda x: x[-1])
    
    parent = [i for i in range(n + 1)]
        
    return graph, parent


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
    graph, parent = get_input()

    result = 0
    for a, b, cost in graph:
        
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
            
    print(result)

if __name__ == "__main__":
    main()
    
    
# 5
# 11 -15 -15
# 14 -5 -15
# -1 -1 -5
# 10 -4 -1
# 19 -4 19