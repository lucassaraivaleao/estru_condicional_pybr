"""
Exercicio-05:
Faça um Programa que leia três números e mostre o maior deles.

Autor: Lucas Leão

"""

primeiro_numero = int(input('Informe o primeiro numero: '))
segundo_numero = int(input('Informe o segundo numero: '))
terceiro_numero = int(input('Informe o terceiro numero: '))

numeros = [primeiro_numero, segundo_numero, terceiro_numero]
maior = 0
for numero in numeros:
    if numero > maior:
        maior = numero
print(f'O maior número foi: {maior}')