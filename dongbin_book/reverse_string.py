def group_num(S):

    group_zero = []
    group_one = []
    group_temp = [S[0]]

    for i in range(1, len(S)):

        if group_temp[-1] == S[i]:
            group_temp.append(S[i])
        else:
            if group_temp[-1] == "1":
                group_one.append(group_temp)
            else:
                group_zero.append(group_temp)
            group_temp = [S[i]]
    if group_temp[-1] == "1":
        group_one.append(group_temp)
    else:
        group_zero.append(group_zero)

    return min(len(group_one), len(group_zero))

        

if __name__ == "__main__":

    S = "000110011101010101011000101"

    result = group_num(S)

    print(result)

