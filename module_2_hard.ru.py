indiana_j = int(input('Введите число, ',))
x = indiana_j//2
chislo = []
delit_ = []
# print(x)
for x in range(1,(x+1)):
    if x != (indiana_j-x):
        chislo.append(x)
        chislo.append(indiana_j-x)
    if (indiana_j % x) == 0 and x > 2:
        delit_.append(x - 1)
        delit_.append(x - (x - 1))

delit_ = delit_ + chislo
#print (chislo)
print (delit_)
