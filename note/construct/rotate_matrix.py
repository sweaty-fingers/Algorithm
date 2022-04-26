def rotate_90(key):
    m = len(key)
    
    li = []
    for r in range(m):
        row_ = []
        for c in range(m):
            row_.append(0)
        li.append(row_)
            
    for i in range(m):
        for j in range(m):
            li[m - 1 - j][i] = key[i][j]
    
    return li

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    print("previous matrix")
    for r in matrix:
        print(r[:])
    matrix = rotate_90(matrix)
    
    print("rotated matrix")
    for r in matrix:
        print(r[:])
    
    
    