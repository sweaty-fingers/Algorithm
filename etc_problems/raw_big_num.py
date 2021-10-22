# 이것이 코딩테스트다 gridy 실전 문제 1 큰 수의 법칙

def max_sum(num_list, M, K):
    
    n_max = M // (K + 1) * K
    n_max += M % (K + 1)
    n_alter = M - n_max

    return num_list[0] * n_max + num_list[1] * n_alter 

if __name__ == "__main__":
    N = 5
    M = 8
    K = 3

    int_list = [2, 4, 5, 4, 6]

    int_list.sort(reverse=True)
    print(int_list)

    result = max_sum(int_list, M, K)

    print(result)
    
