"""
Exercicio-10:
Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
Autor: Lucas Leão

"""
turno = input('Informe o turno no qual você estuda: ')

if turno.lower() == 'matituno' or turno.lower() == 'm':
    print('Bom Dia !')
elif turno.lower() == 'vespertino' or turno.lower() == 'v':
    print('Bom Tarde !')
elif turno.lower() == 'noturno' or turno.lower() == 'n':
    print('Boa Noite !')
else:
    print('Valor inválido !')