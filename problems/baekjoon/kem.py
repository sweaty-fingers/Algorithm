def get_input():
    n = int(input())
    
    students = []
    for _ in range(n):
        name, k, e, m = input().split(" ")
        students.append((name, int(k), int(e), int(m)))
    
    return students


def main():
    
    students = get_input()
    
    students = sorted(students, key=lambda x: x[0])
    students = sorted(students, key=lambda x: x[3], reverse=True)
    students = sorted(students, key=lambda x: x[2])
    students = sorted(students, key=lambda x: x[1], reverse=True)
    
    for i in range(len(students)):
        print(students[i][0])
    
    
if __name__ == "__main__":
    main()