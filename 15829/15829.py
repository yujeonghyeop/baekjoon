n = int(input())
diction = ['0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a = input()
sum = 0
for i,alpha in enumerate(a):
    sum+=(diction.index(alpha)*(31**i))%1234567891
print(sum)