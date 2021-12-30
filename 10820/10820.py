import sys
while(True):
    read = sys.stdin.readline().rstrip('\n')
    so, eo, num, rhd = 0, 0, 0, 0
    if not read:
        break
    for i in range(len(read)):
        if read[i].isupper():
            eo += 1
        elif read[i].islower():
            so += 1
        elif read[i].isdigit():
            num += 1
        else:
            rhd += 1
    print(so, eo, num, rhd)
