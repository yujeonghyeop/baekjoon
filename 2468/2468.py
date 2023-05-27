import sys
from collections import deque

def bfs(arr,x,y,c):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    q=deque()
    q.append([x,y])
    visited[x][y] = c
    while(q):
        a,b = q.popleft()
        for i in range(4):
            ddx = a + dx[i]
            ddy = b + dy[i]
            if ddx < 0 or ddx >= N or ddy < 0 or ddy >= N:
                continue
            else:
                if arr[ddx][ddy] !=0 and visited[ddx][ddy] == -1:
                    visited[ddx][ddy] = c
                    q.append([ddx,ddy])

N = int(input())
town = []
maxnumber = -1
answer = []
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    if max(a) > maxnumber:
        maxnumber = max(a)
    town.append(a)

for i in range(1,maxnumber):    ## 1부터 최대 높이까지 잠길때를 생각해야 하기 때문에 max까지 for문을 돈다
    cnt = []    ## bfs를 돌려주기 위해 넘겨줄 배열
    visited = [[-1]*N for _ in range(N)]
    count = 1   ## visited기록용
    tocal = []  ## i만큼의 침수가 일어나면 안전지역이 몇개인지 세는 배열
    for j in range(N):
        ccnt = []   ## cnt에 추가해주기 위한 배열
        for k in range(N):
            if town[j][k] > i:
                ccnt.append(town[j][k]) ##침수 되지 않았다면 값 그대로 전달
            else:
                ccnt.append(0)  ## 침수 되었다면 0 전달
        cnt.append(ccnt)
    for p in range(N):  ## N만큼 돌면서 침수되지 않고 방문하지 않았다면 bfs돌기
        for q in range(N):
            if cnt[p][q] != 0 and visited[p][q] == -1:
                bfs(cnt,p,q,count)
                count+=1    ## 돌면서 몇번이나 돌았는지를 체크하기 위한 count
    answer.append(count-1)
if len(answer) !=0: ## 하나도 침수되지 않을 수 있다는 예외 사항 적용
    print(max(answer))
else:
    print(1)