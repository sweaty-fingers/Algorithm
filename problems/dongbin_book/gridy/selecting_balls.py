def get_input():
    n, m = map(int, input().split(" "))
    ball_list = list(map(int, input().split(" ")))

    return n, m, ball_list

def main():
    n, m, ball_list = get_input()
    
    count = 0
    for i in range(n):
        for j in range(i, n):
            if ball_list[i] == ball_list[j]:
                continue
            count += 1

    print(count)

def better_solve():
    n, m, ball_list = get_input()
    num_balls = [0] * (m + 1)
    
    for b in ball_list:
        num_balls[b] += 1 

    count = 0
    for i in range(1, m + 1):
        n -= num_balls[i]
        count += num_balls[i] * n

    print(count)

if __name__ == "__main__":
    #main()
    better_solve()