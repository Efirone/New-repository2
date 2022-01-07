summ=0
file=open('Perepis.txt','r')
for i in file:
    L=i.split()
    god=L[3][6:]
    god=int(god)
    if (god<1978):
        print(L[0])
        summ+=1
print(summ)
print()
file.close()



x=int(input('от '))
x1=int(input('до '))
file=open('Perepis.txt','r')
for i in file:
    L=i.split()
    god=L[3][6:]
    god=int(god)
    if (x<=god<=x1):
        print(L[0],' ',L[1],' ',L[2],' ',god)

file.close()