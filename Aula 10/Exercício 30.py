# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
from time import sleep # Bibliotecca para processar "Efeito".
numero = int(input('Me diga um número: '))
resultado = numero % 2 # todo numero % 2 sempré terá resposta 0 para par ou 1 para impar.
print('Processando...')
sleep(1)
print('Carregando...')
sleep(1)
if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é IMPAR'.format(numero)) 
