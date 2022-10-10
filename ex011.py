x = float(input('Qual a largura da parede?'))
y = float(input('Qual a altura da parede?'))
z = x * y
tinta = z / 2
print("Sua parede tem a dimensão de {:.0f}x{:.0f} m², tendo a área de {:.1f}".format(x, y, z))
print('Sendo assim, a tinha tem o valor de R$3,00 p/litro, e cada litro pinta 2 m²')
print('         ')
print('Será necessário {:.1f} litros, equivalente ao total de R${}'.format(tinta, z * 3))
