"""
Exercicio-07:
Faça um programa que pergunte o preço de três produtos
e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

Autor: Lucas Leão

"""

produto_1 = float(input('Informe o preço do primeiro produto: '))
produto_2 = float(input('Informe o preço do segundo produto: '))
produto_3 = float(input('Informe o preço do terceiro produto: '))

produtos = [produto_1, produto_2, produto_3]
produtos.sort()

if produtos[0] == produto_1:
    print('O produrto mais barato foi o primeiro !')

elif produtos[0] == produto_2:
    print('O produrto mais barato foi o segundo !')

elif produtos[0] == produto_3:
    print('O produrto mais barato foi o terceiro !')