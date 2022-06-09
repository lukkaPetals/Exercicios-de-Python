n = 0
cont = 0
tot = 0
while n != 999:
    n = int(input('Digite um número: '))
    cont += 1
    if n == 999:
        cont -= 1
        break
    tot += n  
print(f'Foram {cont} digitados e a soma de todos eles é igual {tot}')
