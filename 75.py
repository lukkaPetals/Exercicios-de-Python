p = 0
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Outro número: '))
d = int(input('Digite mais outro número: '))
t = a, b, c, d

print(f'Os valores foram {t}')
if t.count(9) == 1:
    print(f'O número nove foi digitado {t.count(9)} vez')
else:    
    print(f'O número nove foi digitado {t.count(9)} vezes')
if t.count(3) == 0:
    print('Não teve nenhum número 3')
else:
    print(f'O valor 3 apareceu na posição {t.index(3)}')
for n in t:
    if n % 2 == 0:
        print(f'O número {n} é par')
