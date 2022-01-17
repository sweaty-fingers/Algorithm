def product_or_add(input):

    result = int(input[0])

    add_case = [0, 1]

    for i in input[1:]:
        
        if result in add_case or int(i) in add_case:
            result += int(i)
        else:
            result *= int(i)

    return result





if __name__ == "__main__":
    input = '111112'

    result = product_or_add(input)

    print(result)
