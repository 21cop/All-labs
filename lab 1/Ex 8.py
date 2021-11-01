import math
x1 = int(input('Перший вектор = '))
x2 = int(input('Другий вектор = '))
y1= int(input('Третій вектор = '))
y2 = int(input('Четвертий вектор = '))
result = (x1-x2)**2 + (y1-y2)**2
sqrt = math.sqrt(int(result))
print('Відстань дорівнює = ', sqrt)