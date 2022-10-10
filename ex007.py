''''calcule a nota de dois alunos e faça a sua média'''
'''float usa para numeros flutuantes, que não são inteiros'''
'''int apenas para números inteiros'''
'''(:.1f) para ficar um número apenas o numero flutuantes'''

x = float(input('Digite a nota do primeiro aluno:'))

y = float(input('Digite a nota do segundo aluno:'))

z = (x + y) / 2
print('A média das notas dos alunos são: {:.1f}'.format(z))
