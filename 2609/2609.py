import sys
import math
read = sys.stdin.readline().split()
gcd = math.gcd(int(read[0]), int(read[1]))
print(gcd)
print(gcd*(int(read[0])//gcd)*(int(read[1])//gcd))
