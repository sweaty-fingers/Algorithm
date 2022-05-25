def get_input():
    n, m = map(int, input().split(" "))
    
    graph = []
    
    for a in range(1, n + 1):
        li = list(map(int, input().split(" ")))
        for b, i in enumerate(li, start=1):
            if i == 1:
                graph.append((a, b))
    todo = list(map(int, input().split(" ")))
    parent = [i for i in range(n + 1)]
    
    return graph, parent, todo


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
    graph, parent, todo = get_input()
    
    
    for a, b in graph:
        union_parent(parent, a, b)
    
    
    p = find_parent(parent, todo[0])
    for to in todo[1:]:
        p_tmp = find_parent(parent, to)
        if p_tmp != p:
            print('NO')
            return
    print('YES')
        

if __name__ == "__main__":
    main()
    
# input
# 5 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3

