arr = list(map(int,input('Please print number').split()))
parni = []
neparni = []
for i in arr:
    if i%2 == 0:
        parni.append(i)
    else:
        neparni.append(i)
print('Парні = ', parni, 'Непарні = ', neparni)