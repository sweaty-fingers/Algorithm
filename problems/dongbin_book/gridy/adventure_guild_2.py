def get_input():
    n = int(input())
    status_list = list(map(int, input().split(" ")))

    return status_list

def grid_search(status_list):
    status_list.sort()

    num_to_go = -1
    num_of_group = 0
    group_temp = []
    last_index = 0
    for i in status_list:
        num_to_go = max(i, num_to_go)
        group_temp.append(i)

        if len(group_temp) >= num_to_go:
            num_of_group += 1
            num_to_go = -1
            group_temp = []
            last_index = i + 1

        if num_to_go > len(status_list) - last_index:
            break
    
    return num_of_group

def main():
    status_list = get_input()
    print(grid_search(status_list))

    return

if __name__ == "__main__":
    main()