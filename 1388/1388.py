import sys

def dfs(room, visited,a,b,count):
    if visited[a][b] ==0:
        visited[a][b] = count
    if room[a][b] == "-":
        if b<len(room[a])-1:
            if room[a][b+1] == "-" and visited[a][b+1] ==0:
                visited[a][b+1] = count
                dfs(room, visited,a,b+1,count)
    elif room[a][b] == "|":
        if a<len(room)-1:
            if room[a+1][b] == "|" and visited[a+1][b] ==0:
                visited[a+1][b] = count
                dfs(room, visited,a+1,b,count)


a,b = sys.stdin.readline().split()
room = [[]for _ in range(int(a))]
for i in range(int(a)):
    c = list(str(sys.stdin.readline().split()))
    for j in range(2, int(b)+2):
        room[i].append(c[j])
visited = [[0]*int(b) for _ in range(int(a))]
count = 1
for j in range(int(a)):
    for k in range(int(b)):
        dfs(room, visited,j,k,count)
        count+=1
answer =[]
for p in range(int(a)):
    for q in range(int(b)):
        answer.append(visited[p][q])
answer = list(set(answer))
print(len(answer))