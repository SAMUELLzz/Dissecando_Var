a = input('Digite algo: ')
print('Otipo primitivo desse valor é: ', type(a))
print('Só tem espaços? ', a.isspace())
print('é um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúscula?', a.islower())
print('Está capitalizada? ', a.istitle()