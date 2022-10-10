x = float(input('Digite um número em metros:'))
'''''''vezes 100 para centímetros'''
'''vezes 1000 para milimetros'''
cm = x * 100
mm = x * 1000

print('O valor de {:.0f} metros, equivale a {:.0f} centímetros e {:.0f} milímetros.'.format(x,cm,mm))
