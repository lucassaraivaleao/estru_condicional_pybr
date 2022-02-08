"""
Exercicio-03:
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

Autor: Lucas Leão

"""
def verificar_sexo(letra):
    if letra.upper() == 'M':
        return f'O sexo é masculino'
    elif letra.upper() == 'F':
        return f'O sexo é feminino'
    else:
        return f'Letra inválida !'

sexo = input('Informe a letra correspondente a seu sexo (M/F): ')

print(verificar_sexo(sexo))