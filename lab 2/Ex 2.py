import math

print('Уведіть цифри в рівнянні')
print('Формула = ', 'ax**2 + bx +c = 0')
a = float(input('Уведіть число '))
b = float(input('Уведіть число '))
c = float(input('Уведіть число '))
discr = (b **2) - (4*a*c) 
print('Дискримінант = ', discr)
if discr >0:
    y1 = (-b +math.sqrt((discr))) / (2 * a)
    y2 = (-b - math.sqrt((discr))) / (2 * a)
    print('Відповідь: Дискримінант =', discr, 'y1 =', y1, 'y2 = ', y2)
if discr == 0:
    x1 = -b /(2*a)
    print('Відповідь: Дискримінант = ', discr, 'x1 = ', x1)
if discr <0:
    print('Відповідь: Коренів немає')
