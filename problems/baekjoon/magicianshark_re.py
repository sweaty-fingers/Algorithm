from collections import deque

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
move_for_indices = [(0, 1), (1, 0), (0, -1), (-1, 0)]

pos_ind_mapping = {}
ind_pos_mapping = {} 

result = 0

def get_input():
    n, m = map(int, input().split(" "))
    
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split(" "))))
    
    magics = deque([])
    
    for _ in range(m):
        magics.append(list(map(int, input().split(" "))))
        
    indices_graph, beads = make_index(graph)
        
    return graph, indices_graph, magics, beads


def make_index(graph):
    len_n = len(graph)
    indices_graph = [[0] * len_n for _ in range(len_n)]
    beads = [0] * len_n * len_n

    q = deque([(0, 0)])
    
    d = 0
    ind = len_n * len_n - 1
    while q and ind >= 0:
        y, x = q.popleft()
    
        for _ in range(4):
            
            dy, dx = move_for_indices[d]
            y_tmp, x_tmp = y + dy, x + dx
            
            if not ((0 <= y_tmp < len_n) and (0 <= x_tmp < len_n)):
                d = (d + 1) % 4
                continue
            
            if indices_graph[y_tmp][x_tmp] != 0:
                d = (d + 1) % 4
                continue
            
            break
        
        indices_graph[y][x] = ind
        pos_ind_mapping[(y, x)] = ind
        ind_pos_mapping[ind] = (y, x)
        beads[ind] = graph[y][x]
        ind -= 1
        q.append((y_tmp, x_tmp))
        
        # print("indices_graph")
        # for g in indices_graph:
        #     print(g[:])
        # input()
        
    return indices_graph, beads


def do_magic_and_shift(magic, beads, len_n):
    beads, num_del = do_magic(magic, beads, len_n)
    # print("beads after magic")
    # print(beads)
    
    beads = shift_beads(beads, num_del)
    # print("beads after shift")
    # print(beads)
    
    #input()
    return beads
    
    
def explode_and_shift(beads):
    num_del = 1
    while num_del:
        beads, num_del = explode(beads)
        # print("beads after explode")
        # print(beads)
        
        beads = shift_beads(beads, num_del)
        # print("beads after shift")
        # print(beads)
        # input()
    return beads


def do_magic(magic, beads, len_n):
    """
    magic은 magics.popleft() 결과를 받는다.
    len_n == n
    """
    py, px = len_n // 2, len_n // 2
    
    d, s = magic
    dy, dx = move[d - 1]
    num_del = 0 
    for i in range(1, s + 1):
        y_tmp, x_tmp = py + i * dy, px + i * dx
        ind = pos_ind_mapping[(y_tmp, x_tmp)]
        beads[ind] = 0
        num_del += 1

    return beads, num_del


def shift_beads(beads, num_del):
    for _ in range(num_del):
        for i in range(1, len(beads) -1):
            if beads[i] == 0:
                beads[i], beads[i + 1] = beads[i + 1], beads[i]

    return beads


def explode(beads):
    global result
    
    conts_beads = []
    cur_bead = -1
    num_del = 0
    
    for i in range(1, len(beads)):
        if cur_bead == -1:
            cur_bead = beads[i]
            conts_beads = []
            conts_beads.append(i)
            
            continue
        
        if beads[i] == cur_bead:
            conts_beads.append(i)
            
        elif beads[i] != cur_bead:
            # print(conts_beads)
            # input()
            if len(conts_beads) >= 4 and cur_bead != 0:
                for ind in conts_beads:
                    beads[ind] = 0
                num_del = num_del + len(conts_beads)
                result += (cur_bead * len(conts_beads))
            
            cur_bead = beads[i]
            conts_beads = [i]

    return beads, num_del


def change_beads(beads):
    len_n = len(beads)
    beads_new = [0] * len_n
    
    cur_bead = -1 
    bead_num = 0
    start = 1
    for b in beads[1:]:
        if start >= len_n:# or b == 0: # or b == 0:을 넣어줌으로서 마지막 부분을 처리 못해서 에러가 나는 현상이 발생! 항상 탈출 조건 주의하기
            break
        
        if cur_bead == -1:
            cur_bead = b
            bead_num = 1
            
            continue
        
        if b == cur_bead:
            bead_num += 1
        else:
            beads_new[start] = bead_num
            beads_new[start + 1] = cur_bead
            
            cur_bead = b
            bead_num = 1
            start += 2
            
    return beads_new


def print_graph(graph):
    print(f"graph")
    for g in graph:
        print(g)
    
    
def print_input(graph, indices_graph, magics, beads):
    
    print_graph(graph)
        
    print("indices_graph")
    for _ in indices_graph:
        print(_)
        
    print("magics")
    for _ in magics:
        print(_)

    print(pos_ind_mapping)
    print(ind_pos_mapping)
    print(beads)
                

def main():
    global result
    graph, indices_graph, magics, beads = get_input()
    #print_input(graph, indices_graph, magics, beads)
    
    len_n = len(graph)
    
    while magics:
        magic = magics.popleft()
        beads = do_magic_and_shift(magic, beads, len_n)
        beads = explode_and_shift(beads)    
        beads = change_beads(beads)
        # print("beads after change")
        # print(beads)
        # input()

    print(result)
    
if __name__ == "__main__":
    main()
        