# 이것이 코딩테스트다 구현 예제 3

if __name__ in "__main__":
    input = input()

    row = input[1]
    col = input[0]

    col_boundary = ["a", "h"]
    row_boundary = ["1", "8"]

    count = 0

    if ord(col) + 2 <= ord("h"):
        if int(row) + 1 <= 8:
            count += 1
        if int(row) - 1 >= 1:
            count += 1
    if ord(col) - 2 >= ord("a"):
        if int(row) + 1 <= 8:
            count += 1
        if int(row) - 1 >= 1:
            count += 1
    

    if int(row) + 2 <= 8:
        if ord(col) + 1 <= ord("h"):
            count += 1
        if ord(col) - 1 >= ord("a"):
            count += 1
    if int(row) - 2 >= 1:
        if ord(col) + 1 <= ord("h"):
            count += 1
        if ord(col) - 1 >= ord("a"):
            count += 1

    
    print(count)
    
    



