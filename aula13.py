nome = 'Magnum'
altura = 1.80
peso = 88
imc = peso / altura ** 2

# F-String 
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

