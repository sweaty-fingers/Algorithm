# https://www.acmicpc.net/problem/14501
# 백준 퇴사

from unittest import result


def get_input():
    n = int(input())
    
    meetings = []
    for _ in range(n):
        t, p = map(int, input().split())
        meetings.append((t, p))
        
    return meetings

def dynamics(meetings):
    
    n = len(meetings)
    results = [0] * n
    
    for i, m in enumerate(meetings[::-1]):
        t, p = m
        
        if (i + 1) < t:
            continue
        
        results[n - (i + 1)] = p + max(results[n - (i + 1) + t:] + [0])
    
    #print(results)
    return max(results)

def main():
    meetings = get_input()
    m = dynamics(meetings)
    
    print(m)


if __name__ == "__main__":
    main()
