# -*- coding: utf-8 -*-

k = float(input('Quantos kilometros foram corridos?:'))
d = int(input('Quantos dias foram passados com o veiculo?:'))

d1 = 60 * d
k1 = 0.15 * k
t = k1 + d1

print('O total a pagar referente ao aluguel do seu carro é igual a: R${}'.format(t))