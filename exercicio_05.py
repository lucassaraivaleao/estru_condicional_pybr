"""
Exercicio-05:
Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:

* A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
* A mensagem "Reprovado", se a média for menor do que sete;
* A mensagem "Aprovado com Distinção", se a média for igual a dez.

Autor: Lucas Leão

"""

primeira_nota_parcial = float(input('Entre com a primeira nota parcial: '))
segunda_nota_parcial = float(input('Entre com a segunda nota parcial: '))

media = (primeira_nota_parcial + segunda_nota_parcial) / 2

if media == 10:
    print('Aprovado com distinção')
elif media >=7:
    print('Aprovado !')
else:
    print('Reprovado ! ')

print(f'Sua média foi: {media}')