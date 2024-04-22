valor = float(input('me informe um valor em metros: '))

print('{}m vai ser agora convertido em todas as medidas possíveis:'.format(valor))

print('{} quilômetros'.format(valor/1000))
print('{} centímetros'.format(valor*100))
print('{} milímetros'.format(valor*1000))