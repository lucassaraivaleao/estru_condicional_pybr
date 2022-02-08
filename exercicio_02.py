"""
Exercicio-02:
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

Autor: Lucas Leão

"""

def verificar_numero(numero):
    if numero >=1:
        status = 'positivo'
    else:
        status = 'negativo'
    return f'O número {numero} é {status}'

numero = int(input('Informe um número inteiro: '))
print(verificar_numero(numero))