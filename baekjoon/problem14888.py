#백준
#연산자 끼워넣기
#https://www.acmicpc.net/problem/14888\
    
from collections import deque

operations = ["+", "-", "*", "//"]

def get_input():
    N = int(input())
    num_list = list(map(int, input().split(" ")))
    oper_list = list(map(int, input().split(" ")))

    return deque(num_list), oper_list

def dfs(num_list, oper_list):
    
    results = []
    oper_num = 0
    
    queue = deque([])
    queue.append([0, 0, 0, 0, num_list.popleft()])
    next = num_list.popleft()
    
    while queue:
        cur = queue.popleft()
        
        if num_list and sum(cur[:-1]) > oper_num:
            next = num_list.popleft()
            oper_num = sum(cur[:-1])
        
        if sum(cur[:-1]) == sum(oper_list):
             results.append(cur[-1])
        
        for i in range(len(operations)):
            if cur[i] >= oper_list[i]:
                continue
            cur_temp = cur[:]
            
            if i == 3 and cur[-1] < 0:
                cur_temp[-1] = -1 * ((-1 * cur[-1]) // next)
            else:
                cur_temp[-1] = eval(f"{cur[-1]} {operations[i]} {next}")
            cur_temp[i] = cur[i] + 1
            #print(f"{cur[-1]} {operations[i]} {next} = {cur_temp[-1]}")
            queue.append(cur_temp)
    
    return max(results), min(results)
                
def main():
    num_list, oper_list = get_input()
    max_num, min_num = dfs(num_list, oper_list)

    print(max_num)
    print(min_num)
    
if __name__ == "__main__":
    main()
    
    