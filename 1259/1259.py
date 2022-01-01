import sys

while(True):
    a = sys.stdin.readline().rstrip('\n')
    if (a == '0'):
        break
    else:
        if (a == a[::-1]):
            print('yes')
        else:
            print('no')
