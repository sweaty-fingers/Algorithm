# 이것이 코딩테스트다 gridy 실전문제 3 : 1이 될 때까지

if __name__ == "__main__":


    n, k = map(int, input().split())

    min_count = 0

    while True:

        if n % k  == 0:
            n = n // k
            min_count += 1

            print(f"n : {n * k} to {n}")
            print(f"min_count : {min_count}")
            print()

        else:
            n -= 1
            min_count +=1

            print(f"n : {n + 1} to {n}")
            print(f"min_count : {min_count}")
            print()

        
        if n == 1:
            break

    print(min_count)

        



