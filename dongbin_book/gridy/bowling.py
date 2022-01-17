import time

def comb(M):
    
    balls = list(map(int, M.split(' ')))

    count = 0
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            if balls[i] == balls[j]:
                continue

            count += 1

    return count

def comb_2(M):
    balls = list(map(int, M.split(' ')))
    n = len(balls)

    balls_list = [0] * 11

    for i in balls:
        balls_list[i] += 1

    count = 0

    for i in range(1, 11):
        n -= balls_list[i]
        count += n * balls_list[i]

    return count

if __name__ == "__main__":
    N = "5"
    M = "1 5 3 3 2 4 5 2 5 3 1 2 3 4 2 1 3 4 1 3 4 2 4 1 5 2 3 3 4"

    start_time = time.time()
    result = comb(M)
    #result = comb_2(M)
    
    print(f"수행 시간 : {time.time() - start_time}")
    print(result)