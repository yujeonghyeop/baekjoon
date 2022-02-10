a,b = list(map(int, input().split()))
house=[]
for i in range(a):
    house.append(int(input()))
house.sort()
print(house)