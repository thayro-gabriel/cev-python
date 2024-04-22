variable = str(input('digite qualquer coisa: '))

print('A palavra digitada é: ', type(variable))

if variable.isspace() == True:
    print('Só tem espaços? Sim')
elif variable.isspace() == False:
    print('Só tem espaços? Não')

if variable.isnumeric() == True:
    print('É numérico? Sim')
elif variable.isnumeric() == False:
    print('É numérico? Não')

if variable.isalpha() == True:
    print('É alfabético? Sim')
elif variable.isalpha() == False:
    print('É alfabético? Não')

if variable.isalnum() == True:
    print('É alfanumérico? Sim')
elif variable.isalnum() == False:
    print('É alfanumérico? Não')

if variable.isupper() == True:
    print('É maiúscula? Sim')
elif variable.isupper() == False:
    print('É maiúscula? Não')

if variable.islower() == True:
    print('É minúscula? Sim')
elif variable.islower() == False:
    print('É minúscula? Não')

if variable.istitle() == True:
    print('É capitalizado? Sim')
elif variable.istitle() == False:
    print('É capitalizado? Não')