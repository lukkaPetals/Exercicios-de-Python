cont = 0
cont2 = 0
expr = str(input('Digite a expressão: '))
for s in expr:
    if s == '(':
        cont += 1
    if s == ')':
        cont2 += 1
if cont == cont2:
    print('Sua expressão esta correta')
else:
    print('Sua expressão esta incorreta')