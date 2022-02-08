"""
Exercicio-04:
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

Autor: Lucas Leão

"""

vogais = ['a', 'e', 'i', 'o', 'u']
def verificar_letra_v_c(letra):
    if letra in vogais:
        print('Você digitou uma vogal !')
    else:
        print('Você digitou uma consoante')

letra = input('Informe uma letra: ')

while len(letra) != 1:
    letra = input('Informe apenas uma letra: ')
    if len(letra) == 1:
        verificar_letra_v_c(letra)
