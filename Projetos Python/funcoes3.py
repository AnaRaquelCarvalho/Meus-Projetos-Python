print('='*8,' Calculando valores com Operadores Aritméticos ','='*8)

# Exercicio com as funções para quebrar linhas (\n)
n1 = float(input('Informe um número: '))
n2 = float(input('Informe outro número: '))
s = n1 + n2
m = n1 * n2
d = n1/n2
divInt = n1//n2
Exp = n1**n2
print(' A soma = {}, \n A multiplicação = {},\n A divisão = {},\n'
' A divisão Inteira = {},\n O expoente = {},\n'.format(s,m,d, divInt, Exp))
print('-'*68)

# Continuar não quebrar a linha com (end = '') ou (end='>>>')

n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))
s = n1 + n2
m = n1 * n2
d = n1/n2
divInt = n1//n2
Exp = n1**n2
print('A soma = {} , A multiplicação = {}, A divisão = {}, A divisão Inteira = {}, O expoente = {} \n'.format(s,m,d, divInt, Exp) , end='')
print('-'*68)