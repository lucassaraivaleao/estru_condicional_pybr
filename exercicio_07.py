"""
Exercicio-07:
Faça um Programa que leia três números e mostre o maior e o menor deles.

Autor: Lucas Leão

"""

primeiro_numero = int(input('Informe o primeiro numero: '))
segundo_numero = int(input('Informe o segundo numero: '))
terceiro_numero = int(input('Informe o terceiro numero: '))

numeros = [primeiro_numero, segundo_numero, terceiro_numero]
numeros.sort()
print(f'O maior número foi: {numeros[-1]} e o menor {numeros[0]}')