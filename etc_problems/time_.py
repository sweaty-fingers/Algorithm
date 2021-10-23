# 이것이 코딩테스트다 구현 예제 2

if __name__ == "__main__":
    N = int(input())

    time = 0
    minute = 0
    seconde = 0

    num = 0

    for t in range(N + 1):
        for m in range(60):
            for s in range(60):
                if "3" in str(t) or "3" in str(m) or "3" in str(s): # if "3" in str(t) + str(m) + str(s) 로 대체 할 수 있음.
                    print(f"{t}:{m}:{s}")
                    num += 1
                    print(f"num : {num}")
                    print()

    
    print(f"output : {num}")






