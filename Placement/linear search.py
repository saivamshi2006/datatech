l = list(map(int, input().split()))
search = int(input())

flag = 0

for i in range(0, len(l)):
    if l[i] == search:
        flag = 1
        print("I found my element at", i, "index")
        break

if flag == 0:
    print("Element is not found")
