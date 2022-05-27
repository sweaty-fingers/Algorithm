# 탑승구

def get_input():
    G = int(input())
    P = int(input())

    planes = [int(input()) for _ in range(P)]
    
    
    return planes, G


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
    planes, n_gates = get_input()
    
    parent = [0] * (n_gates + 1)
    for i in range(len(parent)):
        parent[i] = i
    
    
    count = 0
    print(parent)
    
    for p in planes:
        
        if p > n_gates:
            p = n_gates
            
        p_parent = find_parent(parent, p)
        if p_parent == 0:
            break
        
        union_parent(parent, p_parent - 1, p)
        print(f"p: {p}")
        count += 1
        print(f"count: {count}")
        print(parent)
        print("-" * 30)
        
    
    print(count)
    
if __name__ == "__main__":
    main()