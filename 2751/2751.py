def quicksort(array):
    if len(array)<=1:
        return array
    pivot =array[0]
    tail =array[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot] 
    return quicksort(left_side) + [pivot] + quicksort(right_side)

array=[]
n=int(input())
for i in range(n):
    array.append(int(input()))
array1=quicksort(array)
for j in range(n):
    print(array1[j])