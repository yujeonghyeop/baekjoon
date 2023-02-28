n = int(input())
building = []
answer = 0
for i in range(n):
    h = int(input())
    if len(building) == 0:
        building.append(h)
    else:
        if building[-1] > h:
            answer += len(building)
            building.append(h)
        else:
            building.pop()
            while(True):
                if len(building) == 0:
                    building.append(h)
                    break;
                else:
                    if building[-1] > h:
                        answer += len(building)
                        building.append(h)
                        break
                    else:
                        building.pop()
print(answer)