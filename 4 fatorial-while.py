n = int(input('Digite um número: '))
f = 1
c = 1
while c <= n:
    f = f * c
    c = c + 1
    print('{}! = {}'.format(c - 1, f))