n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
me = (n1 + n2) / 2
if me < 5:
    print('A média foi {}\nAluno reprovado!'.format(me))
elif 5 < me < 6.9:
    print('A média foi {}\nAluno está de recuperação!'.format(me))
elif me >= 7:
    print('A média foi {}\nAluno aprovado!'.format(me))