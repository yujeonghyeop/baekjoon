num = int(input())
answer = 0
for i in range(num):
    heap = []
    check = True
    a = input()
    for j in range(len(a)):
        if a[j] not in heap:
            heap.append(a[j])
        elif a[j] in heap and a[j-1] == a[j]:
            continue
        else:
            check = False
    if check:
        answer += 1
print(answer)
