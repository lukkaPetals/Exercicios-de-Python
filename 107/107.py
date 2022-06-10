"""Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções."""

import moeda


print("[1] Aumento")
print("[2] Diminuir")
print("[3] Dobro")
print("[4] metade")

opção = int(input("Escolha qual operação você deseja fazer?: "))

if opção == 1:
    num = int(input("Qual número você deseja aumentar?: "))  
    times = int(input("Por quantas vezes?: "))
    moeda.aumentar(num, times)

if opção == 2:
    num = int(input("Qual número você deseja diminuir?: "))
    minus = int(input("Você quer diminuir por quantos?: "))
    moeda.diminuir(num, minus)

if opção == 3:
    num = int(input("Qual o número você deseja dobrar?: "))
    moeda.dobro(num)

if opção == 4:
    num = int(input("Qual o número você deseja minuir pela metade?: "))
    moeda.metade(num)

