# 이것이 코딩테스트다 gridy 예제 3-1

import collections
def minimum_coin_num(n, coins):
    
    total_coin = 0
    coin_dict = collections.defaultdict(int)
    
    for coin in coins:
        num_coin = n // coin
        total_coin += num_coin
       
        n %= coin
       
        coin_dict[coin] = num_coin
       
        if n == 0:
            print(coin_dict)
            print(f"Number of coin : {total_coin}")
            return total_coin


if __name__ == "__main__":
    n = 1260
    coins = [500, 100, 50, 10]

    result = minimum_coin_num(n, coins)
