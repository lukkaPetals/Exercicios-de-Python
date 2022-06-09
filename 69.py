cont18 = 0
contM = 0
contIdaMul = 0
programa = True

while programa == True:
    print('Cadastro de Uma pessoa')
    idade = int(input('Digite a idade dessa pessoa: '))
    if idade >= 18:
        cont18 += 1
    sexo = str(input('Qual o sexo dessa pessoa? [M/F] ').upper().strip())
    if sexo == 'M':
        contM += 1
    if sexo == 'F' and idade < 20:
        contIdaMul += 1
    continuar = str(input('Deseja continuar o cadastramento? [S/N] ')).upper().strip()
    if continuar == 'N':
        break

print('Resultado dos Dados')
print(f'Tiveram {cont18} pessoas com 18 anos ou mais')
print(f'Tiveram {contM} participantes homens')
print(f'Tiveram {contIdaMul} participantes mulheres com menos de 20 anos')
#XD