s = str(input('Digite seu sexo [M/F]: ')).upper().strip()
while s not in 'MmFf':    
    str(input('Erro, digite novamente: ')).upper().strip()
print('Fim')
