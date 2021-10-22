# 이것이 코딩테스트다 gridy 실전문제 2 숫자 카드 게임 


if __name__ == "__main__":
    
    card_list_1 = [[3, 1, 2], [4, 1, 4], [2, 2, 2]]
    card_list_2 = [[7, 3, 1, 8], [3, 3, 3, 4]]

    # for card_list 1
    result_1 = 0

    for row in card_list_1:
        min_value = min(row)

        if min_value > result_1:
            result_1 = min_value
        
    result_2 = 0

    for row in card_list_2:
        min_value = min(row)

        if min_value > result_2:
            result_2 = min_value
    

    print(f"Result_1 : {result_1}")
    print(f"Result_2 : {result_2}")

