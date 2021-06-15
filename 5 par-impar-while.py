import random
n = c = 0
while n >= 0:
    c += 1
    n = int(input('Digite um número: '))
    poi = str(input('Par ou Impar (sem acento)? ')).upper().strip()[0]
    a = random.randint(1, 10)
    soma = n + a
    if poi not in 'PpIi':
        print('Opção inválida.')
        break
    print(f'O escolhido foi {n}\nO aleatório foi {a}\nA soma deles é {soma}')
    if soma % 2 == 0:
        print('Par.')
    if soma % 2 == 1:
        print('Ímpar.')
    if poi == 'P' and soma % 2 == 0:
        print('Você ganhou!')
    if poi == 'I' and soma % 2 == 1:
        print('Você ganhou!')
    elif poi == 'P' and soma % 2 == 1 or poi == 'I' and soma % 2 == 0:
        print(f'Você perdeu! :(\nFim de jogo! Você venceu {c - 1} vezes!')
        break
