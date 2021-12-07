alpha = str(input())
alpha = alpha.replace('c=', 'c').replace('c-', 'C').replace('dz=', 'D').replace(
    'd-', 'd').replace('lj', 'l').replace('nj', 'n').replace('s=', 's').replace('z=', 'z')
print(len(alpha))
