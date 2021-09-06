import collections
str1=input().lower()
str2=input().lower()
c1=collections.Counter(str1)
c2=collections.Counter(str2)
flag=0 #flag variable
for c in c1:#for loop
    print(c,c1[c])
    if c1[c] != c2[c]:
        flag=1
if flag==0:
    print("Anagram")
else:
    print("Not Anagram")

