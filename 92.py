from datetime import datetime
ano = datetime.now().year
funcionario = {}
funcionario['nome'] = str(input('Nome: '))
funcionario['ano'] = int(input('Ano de nascimento: '))
funcionario['Idade'] = ano - funcionario['ano']
funcionario['carteira'] = int(input('Carteira de trabalho(Caso não tenha, digite 0): '))
if funcionario["carteira"] != 0:
    funcionario['contratação'] = int(input('Ano de contratação: '))
    funcionario['sálario'] = float(input('Sálario: R$'))
    funcionario['aposentadoria'] = funcionario['Idade'] + ((funcionario["contratação"] + 15) - ano)
print('-=' * 30)
for k, v in funcionario.items():
    print(f' - {k} tem o valor {v}')
print('-=' * 30)
