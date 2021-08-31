fibarray = [0,1]
def fibo(n):
    if(n<0):
        print("Incorrect Input")
    elif n<= len(fibarray):
        return fibarray[n-1]
    else:
        temp_fib = fibo(n-1) + fibo(n-2)
        fibarray.append(temp_fib)
        return temp_fib
n=int(input())
print(fibo(n))

