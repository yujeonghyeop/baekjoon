x, y, w, h = map(int, input().split())
answer = []
answer.append(x-0)
answer.append(y-0)
answer.append(w-x)
answer.append(h-y)
print(min(answer))
