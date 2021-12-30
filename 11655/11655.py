import sys
read = sys.stdin.readline().rstrip('\n')
answer = ''
for i in range(len(read)):
    if read[i].isalpha():
        cnt = ord(read[i])
        if 65 <= ord(read[i]) <= 90:
            cnt += 13
            if cnt > 90:
                cnt -= 26
        elif 97 <= ord(read[i]) <= 122:
            cnt += 13
            if cnt > 122:
                cnt -= 26
        answer += chr(cnt)
    else:
        answer += read[i]
print(answer)
