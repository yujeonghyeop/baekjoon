import sys
n = int(sys.stdin.readline())
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alpha = sys.stdin.readline()
cnt = []
cntstr = ''
for i in range(n):
    c = sys.stdin.readline().split()
    alpha = alpha.replace(alphabet[i], c[0]+' ')
    print(alpha)
for j in range(len(alpha)-1):
    if alpha[j] == '*':
        cnt1 = cnt.pop()
        cnt2 = cnt.pop()
        cnt.append(cnt1*cnt2)
        print(cnt)
    elif alpha[j] == '/':
        cnt1 = cnt.pop()
        cnt2 = cnt.pop()
        cnt.append(cnt2/cnt1)
        print(cnt)
    elif alpha[j] == '+':
        cnt1 = cnt.pop()
        cnt2 = cnt.pop()
        cnt.append(cnt1+cnt2)
        print(cnt)
    elif alpha[j] == '-':
        cnt1 = cnt.pop()
        cnt2 = cnt.pop()
        cnt.append(cnt2-cnt1)
        print(cnt)
    elif alpha[j] == ' ':
        cnt.append(int(cntstr))
        cntstr = ''
    else:
        cntstr += alpha[j]
print("{0:.2f}".format(cnt[0]))
