#-*-coding:utf8;-*-
#qpy:console

Alt = float(input('Digite a altura'))
Lar = float(input('Digite a largura'))
Are = Alt * Lar
Tin = Are / 2

print('Para pinta essa parede de {:.3} metros quadrados, será necessário {:.3} litros de tinta'.format(Are,Tin))

Per = float(input('Digite o preço R$:'))
Des = Per * 0.05
Tot = Per - Des
print ('O valor total com desconto é R$:{}'.format(Tot))

Sal = float(input('Digite seu salário antes do aumento: R$'))
Aum = Sal + (Sal * 0.15)

print('Seu salário atual é R$: {}'.format(Aum))

