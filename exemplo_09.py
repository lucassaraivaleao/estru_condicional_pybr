"""
Exercicio-09:
Faça um Programa que leia três números e mostre-os em ordem decrescente.

Autor: Lucas Leão

"""

primeiro_numero = int(input('Informe o primeiro numero: '))
segundo_numero = int(input('Informe o segundo numero: '))
terceiro_numero = int(input('Informe o terceiro numero: '))

numeros = [primeiro_numero, segundo_numero, terceiro_numero]
numeros.sort()
numeros.reverse()

print(numeros)