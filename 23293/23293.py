import sys
lognum,playernum=input().split()
lognum = int(lognum)
playernum = int(playernum)
area = [1]*(playernum+1)
item = [[] for i in range(playernum+1)]
errlog = []
errplayer = []
for i in range(lognum):
    read = sys.stdin.readline().split()
    log = str(read[0])
    playercode = int(read[1])
    actcode = str(read[2])
    actnum = int(read[3])
    if actcode == 'M':
        area[playercode]=actnum
    elif actcode == 'F':
        if area[playercode]==actnum:
            item[playercode].append(actnum)
        else:
            item[playercode].append(actnum)
            errlog.append(log)
    elif actcode == 'C':
        cnum= int(read[4])
        if actnum in item[playercode]:
            if cnum in item[playercode]:
                item[playercode].remove(cnum)
                item[playercode].remove(actnum)
            else:
                item[playercode].remove(actnum)
                errlog.append(log)
        elif cnum in item[playercode]:
            item[playercode].remove(cnum)
            errlog.append(log)
        else:
            errlog.append(log)
    elif actcode == 'A':
        if area[actnum] == area[playercode]:
            area[actnum]=0
        else: 
            area[actnum]=0
            errlog.append(log)
            errplayer.append(playercode)
if len(errlog)==0:
    print(0)
else:
    print(len(errlog))
    print(' '.join(errlog))
if len(errplayer)==0:
    print(len(errplayer))
else:
    errplayer=list(set(errplayer))
    errplayer.sort()
    print(len(errplayer))
    print(' '.join(map(str,errplayer)))