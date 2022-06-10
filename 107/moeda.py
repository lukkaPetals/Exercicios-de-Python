"""Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções."""

def aumentar(num, times):
    print(f'O número {num} foi aumentado em {times} vezes, dando o número {num * times}')


def diminuir(num, minus):
    print(f'O número {num} foi diminuido por {minus} , dando o número {num + minus}')


def dobro(num):
    print(f'O número {num} foi dobrado, dando o número {num * 2}')


def metade(num):
    print(f'A metade do número {num} é {num / 2}')


