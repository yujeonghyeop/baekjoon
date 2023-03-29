N = int(input())
rofe = []
maxrofe = -1
for i in range(N):
    a = int(input())
    rofe.append(a)
rofe = sorted(rofe)
for j in range(N,0,-1):
    if rofe[N-j] * j > maxrofe:
        maxrofe = rofe[N-j] * j
print(maxrofe)