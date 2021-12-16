def factorial(x):
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)


a = int(input())
if a == 0:
    print(1)
else:
    print(factorial(a))
