porextenso = ('zero', 'um', 'dois', 'três', 'quatro', 'quatro' 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número de 0 a 20: '))
    if 0 <= n <= 20:
        break
    print('Erro! tente novamente')
print(f'O número {n} por extenso é {porextenso[n]}')
