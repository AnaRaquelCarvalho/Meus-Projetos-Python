print('====== Funções do Python ======')

# Espaços entre as palavras (20 vezes)
nome = input('Qual o seu nome: ')
print(' Olá {:20}!!! Tudo bem com você?'.format(nome))
print('---------------------------------------')

# Alinhamento a Direita
nome = input("Qual é o seu nome: ")
print('Boa tarde, {:>20}!'.format(nome))
print('--------------------------------------')

# Alinhamento a Esquerda
nome = input("Qual é o seu time do coração: ")
print('O seu time é o {:<20}. Correto?'.format(nome))
print('--------------------------------------')

# Centralizado
nome = input('Informe algo: ')
print('{:^20}'.format(nome))
print('--------------------------------------')

# Igual colocado 20 vezes
print('='*20)
print('-------------------------------------')

# Palavras juntas
print('Oi'+ 'Olá')
print('Oi,'+ 'Olá')
print('Oi'* 5)

# Potência ou Exponê^nciação
print(pow(4,3))

# Raiz Quadrada
print(81**(1/2))

# Raiz Cúbica
print(127**(1/3))
