a = int(input('Перший зал = '))
b = int(input('Другий зал = '))
c = int(input('Третій зал = '))
d = int(input('Четвертий зал ='))
move = (a//3) + (b//3) + (c//3) + (d//3)
move2 =(a%3) + (b%3) +(c%3) +(d%3)
print('Шакали= ', move)
print('Шакали =', move2)
print('Штанг потрібно = ', move + move2)