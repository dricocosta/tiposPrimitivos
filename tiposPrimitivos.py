n = input('Digite o que quiser: ')
print('O tipo primitivo do valor digitado é:', type(n))
print('O valor digitado é alfanumérico = ', n.isalpha())
print('O valor digitado é número = ', n.isnumeric())
print('está em maiúscula: ', n.isupper())
print('Está em minúscula: ', n.islower())
print('Está capitalizado: ', n.istitle())
print('É somente espaço: ', n.isspace())