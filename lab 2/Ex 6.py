result = 0
deresult = 0
print('Онлайн вікторина - Столиці')
print('Столиця Єгипту?', 'A - Відень', 'Б - Каїр', 'B - листопад')
a = input('Ваш варіант відповіді ')
if a == 'Б':
    result= result + 1
else:
    deresult= deresult + 1
print('Столиця Австралії?', 'A - Ліссабон', 'Б - так', 'В - Канберра')
b = input('Ваш варіант відповіді ')
if b == 'B' or b == 'В':
    result= result +1
else:
    deresult= deresult + 1
print('Столиця Африки?', 'А - Аддіс-Абеба', 'Б - Крим', 'В - Душанбе')
c = input('Ваш варіант відповіді')
if c =='A' or c =='А':
    result = result+ 1
else:
    deresult= deresult + 1
print('Столиця Туреччини?', 'А - Сиктивкар', 'Б - Анкара', 'В - можливо')
d = input('Ваш варіант відповіді ')
if d == 'Б':
    result= result + 1
else:
    deresult= deresult + 1
print('Столиця Ватикану?', 'А - Ватикан', 'Б - Київ', 'В - Сербія')
f = input('Ваш варіант відповіді ')
if f == 'A' or f =='А':
    result= result + 1
else:
    deresult= deresult +1
print('Столиця Сербії?' 'A - Пріштіна', 'Б - Белград', 'B - миротворчий батальйон ООС')
g = input('Введіть ваш варіант відповіді ')
if g == 'Б':
    result= result + 1
else:
    deresult= deresult + 1
print('Тест завершено')
print('Правильних відповідей = ', result, 'Неправильних відповідей = ', deresult)