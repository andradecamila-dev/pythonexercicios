salario = float(input('Qual o seu salário?'))
aumento = float(input('Qual será sua porcentagem de aumento?'))
novo = salario + (salario * aumento / 100)

print('Seu salário atual é R$ {} reais, com o seu ajuste salarial de {} %, seu novo '
      'salário será de R$ {:.2f}'.format(salario, aumento, novo))
