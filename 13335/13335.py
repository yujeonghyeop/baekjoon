from collections import deque
import sys
n,w,L = map(int,sys.stdin.readline().split())
truck = deque(list(map(int,sys.stdin.readline().split())))
bridge = deque()
complete = [] ##완료한 트럭들 저장
tmp = 0 ## 트럭의 무게 계산을 위한 변수
time = 0 ## 시간 재기 위한 변수
for i in range(w): ## 다리 길이 설정
    bridge.append(0)
while(len(complete)!=n): ## 전부다 완료할 때 까지 반복문
    if bridge[0] != 0: ## 맨 앞에 나가야 할 놈이 트럭이라면 해당 분기
        outtruck = bridge.popleft() 
        tmp -= outtruck ## 트럭의 무게들에서 빼기
        complete.append(outtruck)  ## 완료한 배열에 나간 트럭 추가
        bridge.append(0) ## 하나 나갔으니 다리에 0 추가
    else:
        bridge.popleft()    ## 멘 잎에 나가야 할 놈이 트럭이아니라면 해당 분기
        bridge.append(0)    ## 하나 나갔으니 0 추가
    if len(truck) != 0:
        if tmp + truck[0] <= L: ## 현재까지 무게 + 넣어주려는 트럭 무게가 중량을 안넘는다면 해당 분기
            temptruck = truck.popleft() ## 트럭 배열에서 다리에 넣어주기 위해 popleft
            tmp += temptruck    ## 무게 +
            bridge[-1] = temptruck  ## 다리 맨 끝에 넣기
    time += 1
print(time)
            