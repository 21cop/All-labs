a = int(input('Введіть перше число = '))
b = int(input('Введіть друге число = '))
c = int(input('Введіть третє число = '))
if a >b and a >c:
    print('Найбільше число = ',a)
if b >a and b >c:
    print('Найбільше число = ',b)
if c >a and c>b:
    print('Найбільше число = ',c)
if a < b and a < c:
    print('Найменше число = ', a)
if b < a and b <c:
    print('Найменше число = ',b)
if c < a and c <b:
    print('Найменше число = ',c)