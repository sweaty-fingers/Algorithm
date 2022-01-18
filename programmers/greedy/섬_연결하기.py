def solution(n, costs):

    answer = 0
    costs.sort(key=lambda x: x[2])

    cycle_table = {}

    for i in range(n):
        cycle_table[i] = i

    print(cycle_table)
    len_ = 0
    for c in costs:
        c1, c2 = sorted(c[:-1])
        cost = c[-1]

        if cycle_table[c1] == cycle_table[c2]:
            continue

        answer += cost
        len_ += 1

        cy_1 = cycle_table[c1]
        cy_2 = cycle_table[c2]

        if cy_1 > cy_2:
            cy_min = cy_2
            cy_ch = cy_1
        else:
            cy_min = cy_1
            cy_ch = cy_2

        for k, v in cycle_table.items():
            if v == cy_ch:
                cycle_table[k] = cy_min

        if len_ == n - 1:
            break

    return answer
