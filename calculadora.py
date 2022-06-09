# -*- coding: utf-8 -*-
"""
Calculadora
Autor: Lucas Lira
Função: calcular
"""

print("Jarvis v0.2 Alpha Rafael Baitola")

sair = False

while sair == False:

	num1 = input("Digite o primeiro número por favor:")
	num1 = int(num1)
	operador = input("digite agora um operador de sua escolha senhor(a)(+-/*):")
	num2 = input("Digite por favor o segundo número para efetuar por completo o calculo:")
	num2 = int(num2)


	if operador == "+":
		operacao = num1 + num2

	if operador == "-":
		operacao = num1 - num2 

	if operador == "*":
		operacao = num1 * num2


	if operador == "/":
		operacao = num1 / num2

	print("resultado:")
	print(operacao)

	Test = input("deseja sair senhor(a)? (s/n) :")
	if Test == "s":
		break
