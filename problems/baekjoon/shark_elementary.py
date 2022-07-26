adjacent = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def get_input():
    n = int(input())
    student_dict = {}
    
    for _ in range(1, n * n + 1):
        li_tmp = list(map(int, input().split(" ")))
        student_dict[li_tmp[0]] = li_tmp[1:]
    
    graph = [[0] * n for _ in range(n)]
    
    return graph, student_dict, n


def fill_student(graph, student_dict, s):
    """
    like_list: student_dict[i]
    """
    n = len(graph)
    num_like = 0
    num_va = 0
    y_f, x_f = -1, -1
    like_list = student_dict[s]
    for y in range(n):
        for x in range(n):
            if graph[y][x] != 0:
                continue
            
            like_tmp = 0
            va_tmp = 0
            for dy, dx in adjacent:
                y_tmp, x_tmp = y + dy, x + dx
                
                if not ((0 <= y_tmp < n) and (0 <= x_tmp < n)):
                    continue
                
                if graph[y_tmp][x_tmp] in like_list:
                    like_tmp += 1    
                elif graph[y_tmp][x_tmp] == 0:
                    va_tmp += 1
            
            if like_tmp > num_like or y_f < 0 or x_f < 0:
                y_f, x_f = y, x
                num_like = like_tmp
                num_va = va_tmp
            
            elif like_tmp == num_like:
                if va_tmp > num_va:
                    y_f, x_f = y, x
                    num_like = like_tmp
                    num_va = va_tmp
                
    graph[y_f][x_f] = s
    
    return graph


def get_score(graph, student_dict):
    
    n = len(graph)
    score = 0
    
    for y in range(n):
        for x in range(n):
            
            like_tmp = 0
            s = graph[y][x]
            like_list = student_dict[s]
            
            for dy, dx in adjacent:
                y_tmp, x_tmp = y + dy, x + dx
                
                if not ((0 <= y_tmp < n) and (0 <= x_tmp < n)):
                    continue
                
                if graph[y_tmp][x_tmp] in like_list:
                    like_tmp += 1

            if like_tmp > 0:
                score += 10 ** (like_tmp - 1)
        
    return score


def main():
    graph, student_dict, n = get_input()
    
    for s in student_dict:
        graph = fill_student(graph, student_dict, s)
    
    score = get_score(graph, student_dict)
    print(score)
    
if __name__ == "__main__":
    main()