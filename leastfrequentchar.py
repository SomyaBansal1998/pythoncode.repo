from collections import Counter
str1=input()
res=Counter(str1)
res=min(res,key=res.get)
print("Least frequent character is:"+ str(res))


