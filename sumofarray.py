def _sum(arr):
    sum1=0
    for i in arr:
        sum1 = sum1 + i
    return(sum1)
arr=[]
arr = [12,3,4,15]
n = len(arr)
ans = _sum(arr)
print("Sum of the array is ",ans)

