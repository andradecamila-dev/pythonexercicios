x= float(input('Qual o valor do produto: R$'))
y = x * 5/100
z = x - y
print("Seu produto terá 5% de desconto, sendo assim de R${:.2f}, seu desconto será de R$ {:.2f},o novo valor"
      " R${:.2f}".format(x, y, z))