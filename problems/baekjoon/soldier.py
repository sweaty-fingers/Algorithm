# https://www.acmicpc.net/problem/18353
# 백준

def get_input():
    n = int(input())
    
    soldiers = list(map(int, input().split()))
    
    return soldiers


def dynamics(soldiers):
    
    results = []
    for i, s in enumerate(soldiers):
        if i == 0:
            results.append(1)
            continue
        temp = [results[j] for j in range(i) if soldiers[j] > s]
        if temp:
            num = 1 + max(temp)
        else:
            num = 1
        results.append(num)
    
    # print(results)
    return max(results)
        

def main():
    soldiers = get_input()
    max_num = dynamics(soldiers)
    print(len(soldiers) - max_num)
    

if __name__ == "__main__":
    main()