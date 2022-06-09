top20 = ('Atlético-GO', 'Bahia', 'Bragantino', 'Fortaleza', 'Athletico-PR', 'Flamengo', 'Ceará SC', 'Santos', 'Cuiabá', 'Fluminence', 'Sport Recife', 'Internacional', 'Juventude', 'Cuiabá', 'São Paulo', 'Grêmio', 'Atlético-MG', 'América-MG', 'Palmeiras', 'Corinthias', 'Chapecoense')

print(f'Os top 5 do brasileirão hoje são: {top20[:5]}')
print(f'Os 4 ultimos colocados são {top20[-4:]}')
print(f'Ordem alfabetica dos times: {sorted(top20)}')
print(f'O time Chapecoense está em {top20.index("Chapecoense")} lugar')
#use aspas duplas quando precisar usar uma string dentro de outra string