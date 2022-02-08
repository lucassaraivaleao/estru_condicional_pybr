"""
Exercicio-01:
Faça um Programa que peça dois números e imprima o maior deles.

Autor: Lucas Leão

"""
primeiro_numero = int(input('Informe o primeiro número: '))
segundo_numero = int(input('Informe o segundo número: '))

if primeiro_numero > segundo_numero:
    print(f'{primeiro_numero} é maior que {segundo_numero}')
else:
    print(f'{segundo_numero} é maior que {primeiro_numero}')