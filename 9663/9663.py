import sys

def queen(x,y):
    a=[[0 for j in range(n)] for j in range(n)]
    for i in range(n):
        a[x][i] = 1
        a[i][y] = 1
    for i in range(4):
        p = x
        q = y
        if i==0:
            while(True):
                a[p][q] =1
                p-=1
                q-=1
                if p<0 or q<0:
                    break
        elif i==1:
            while(True):
                a[p][q] = 1
                p+=1
                q+=1
                if p>=n or q>=n:
                    break
        elif i==2:
            while(True):
                a[p][q] = 1
                p+=1
                q-=1
                if p>=n or q<0:
                    break
        elif i==3:
            while(True):
                a[p][q] = 1
                p-=1
                q+=1
                if p<0 or q>=n:
                    break
    a[x][y]=0
    print(a)
    cnt=[]
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0:
                cnt.append((i,j))
    answer.append(cnt)

n = int(sys.stdin.readline())
answer=[]
for i in range(n):
    for j in range(n):
        queen(i,j)
print(answer)
print(len(list(set(answer))))
# print(list(set([tuple(set(item))for item in answer])))
# print(len(list(set([tuple(set(item))for item in answer]))))