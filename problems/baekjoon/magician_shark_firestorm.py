from copy import deepcopy

def get_input():
    n, q = map(int, input().split(" "))
    n = 2**n
    
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split(" "))))
        
    for i in range(q):
        stages = list(map(int, input().split(" ")))
    
    return graph, stages
    


def rotate_subgraph(graph, l):
    
    step = 2 ** l
    n = len(graph) // step
    
    rotated_graph = [[0] * len(graph) for _ in range(len(graph))]

    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, step):
                for l in range(0, step):
                    rotated_graph[j * step + k][(n - 1 - i) * step + l] = graph[i * step + k][j * step + l]

            for r in rotated_graph:
                print(r)
            input()
    return rotated_graph
        

def main():
    graph, stages = get_input()
    
    for g in graph:
        print(g)
    
    print(stages)

    rotated_graph = rotate_subgraph(graph, stages[0])
    
    for r in rotated_graph:
        print(r)

if __name__ == "__main__":
    main()