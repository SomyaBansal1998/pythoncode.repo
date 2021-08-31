def findminsum(num):
    sum1=0
    i=2
    while(i*i<=num):
        while(num%i==0):
            sum1+=i
            num/=i
        i+=1
    sum1+=num
    return sum1
num=int(input())
print(findminsum(num))
