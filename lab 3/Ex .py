a = print('Доступні фігури: Тура, Кінь, Слон, Ферзь, Король.')
name = input('Введіть бажану фігуру: ')
x1 = int(input('Координата x1= '))
y1 = int(input('Координата y1 = '))
x2 = int(input('Координата x2 = '))
y2 = int(input('Координата y2 = '))
if name == 'Тура' or name =='тура':
    if x1 == x2 or y1 == y2:
        print('Хід для тури є  доступним')
    else: 
        print('Хід для тури недоступний')
 #Кінь       
if name == 'Кінь' or name =='кінь':    
    dx = abs(x1-x2)
    dy = abs(y1-y2)
    if dx == 1 and dy == 2 or dx == 2 and dy == 1:
        print('Хід для коня є доступним')
    else:
        print('Хід для коня є недоступним') 
#Слон
if name == 'Слон' or name == 'слон':
    if abs(x1-x2) == abs(y1-y2):
     print('Хід для слона є доступним')
    else:
        print('Хід для слона є недоступним')
#Ферзь
if name == 'Ферзь' or name == 'ферзь':
    if x1 ==x2 or y1 == y2 or abs(x1-x2)== abs(y1-y2):
        print('Хід для ферзя є доступним')
    else:
        print('Хід для ферзя є недоступним')
#Король
if name == 'Король' or name == 'король':
    if abs(x1-x2)>1 or abs(y1-y2)>1:
        print('Хід для короля є доступним')
    else:
        print('Хід для короля є недоступним')