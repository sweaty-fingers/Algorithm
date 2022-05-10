array = [7, 5, 9, 0, 3, 1, 6, 3, 9, 1, 4, 8, 0 , 5, 2]

count = [0] * (max(array) + 1)

print("previous array")
print(array)
for a in array:
    count[a] += 1

print("array sorted")
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=" ")
        
