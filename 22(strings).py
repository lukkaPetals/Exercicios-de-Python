nome = str(input('Digite o nome completo')).strip()
print('Analisando seu nome...')
print('Seu nome em maiusculas eh {}'.format(nome.upper()))
print('Seu nome minusculas eh {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome eh {} e ele tem {} letras'.format(separa[0],len(separa[0])))