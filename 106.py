while True:
   a = input(str('Digite o nome da função que você precisa: '))
   help(a)
   fim = input(str('Deseja continuar? [S/N]: ')).upper().strip()
   if fim == 'n':
       break
