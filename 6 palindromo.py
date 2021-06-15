f = str(input('Digite uma frase: ')).strip().lower()
rep = f.replace(' ', '')
print(rep)
pr = rep[0]
se = rep[1]
te = rep[2]
ul = rep[-1]
pe = rep[-2]
an = rep[-3]
if pr == ul and se == pe and te == an:
    print('"{}" é um palíndromo!'.format(f))
else:
    print('"{}" NÃO é um palíndromo!'.format(f))
