# 백준 정수 삼각형
# https://www.acmicpc.net/problem/1932

def get_input():
    n = int(input())
    
    triangle = []
    
    for i in range(n):
        t = list(map(int, input().split()))
        triangle.append(t)
    
    return triangle


def dynamics(triangle):
    
    n = len(triangle)
    results = []
    for cur in range(n - 1, -1, -1):
        if cur == n - 1:
            results.append(triangle[n - 1])
            continue
            
        t = triangle[cur]
        t_down = triangle[cur + 1]
        
        t_len = len(t)
        
        for i in range(t_len):
            t[i] = max(t_down[i] + t[i], t_down[i + 1] + t[i])
    
    return triangle


def main():
    
    triangle = get_input()
    triangle = dynamics(triangle)
    print(triangle[0][0])
    

if __name__ == "__main__":
    main()
