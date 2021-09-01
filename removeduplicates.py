from collections import Counter
 
def removeduplicates(str1):
    str1 = str1.split(" ")
    for i in range(0, len(str1)):
        str1[i] = "".join(str1[i])
    UniqW = Counter(str1)
    s = " ".join(UniqW.keys())
    print (s)
str1=input()
removeduplicates(str1)
