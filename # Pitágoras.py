# Pitágoras

from math import hypot

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjascente: '))

hi = hypot(co, ca)

print('O valor da hipotenusa é igual a {}'.format(hi))
