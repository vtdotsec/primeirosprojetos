print('1.Binário\n2.Octal\n3.Hexadecimal\n')
op = int(input('Escolha uma opção: '))
n = int(input('Escreva um número inteiro: '))
if op == 1:
    print('O número {} em Binário é {}'.format(n, bin(n)[2:]))
elif op == 2:
    print('O número {} em Octal é {}'.format(n, oct(n)[2:]))
elif op == 3:
    print('O número {} em Hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida.')
