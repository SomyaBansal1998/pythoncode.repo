def uncommon(a,b):
    lista = a.split()
    listb = b.split()
    uc = ''
    for i in lista:
        if i not in listb:
            uc = uc+" "+i
    for j in listb:
        if j not in lista:
            uc = uc+" "+j
  
    return uc
a = input()
b = input()
print(uncommon(a,b))
