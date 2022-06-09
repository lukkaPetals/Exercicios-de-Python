def notas(*n, sit=False):
    boletim = dict()
    boletim['Total'] = len(n)
    boletim['maior'] = max(n)
    boletim['menor'] = min(n)
    boletim['média'] = sum(n) / len(n)
    print(boletim)
    if sit == True:
        if boletim['média'] >= 7:
            print('A turma foi aprovada')
        if boletim['média'] < 4:
            print('A turma foi reprovada')
        if boletim['média'] >= 4 and boletim['média'] < 7:
            print('A turma está em recuperação')
    else:
        sit = False
    

#Programa principal
resp = notas(7, 7, 8, 9, sit=True)
