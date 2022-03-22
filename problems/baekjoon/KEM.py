# https://www.acmicpc.net/problem/10825
# 국영수

def get_input():
    N = int(input())
    
    li = []
    for _ in range(N):
        name, korean, english, math = input().split(" ")
        korean, english, math = int(korean), int(english), int(math)
        li.append([-1 * korean, english, -1 * math, name])
        
    return li

def main():
    li = get_input()
    li.sort()
    
    for i in li:
        print(i[-1])


if __name__ == "__main__":
    main()
        