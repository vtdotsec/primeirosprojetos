# WIP
# EM PROGRESSO...
from random import randint
from forex_python.converter import CurrencyRates
import datetime
print('\nCONVERSOR "UNIVERSAL"\n')
op = int(input('Escolha o que deseja fazer:\n'
               '1. TEXTO\n'
               '2. MEDIDAS\n'
               '3. MOEDAS\n'
               '4. FÓRMULAS\n'
               '5. NÚMEROS ALEATÓRIOS\n'
               '6. SAIR DO PROGRAMA\n'
               'Digite uma opção: '))
if op == 1:
    print('*' * 20)
    print('\nCONVERSOR DE TEXTO')
    texto = str(input('Digite o texto para converter: '))
    print(f'Seu texto é {texto}\n')
    optexto = int(input('Digite o que fazer com seu texto:\n'
                            '1. MAIÚSCULO\n'
                            '2. MINÚSCULO\n'
                            '3. CAPITALIZAR (Primeira letra da frase MAIÚSCULA)\n'
                            '4. TÍTULO (Primeira letra de cada palavra MAIÚSCULA)\n'
                            '5. SAIR (Sair do programa)\n'
                            'Digite uma opção: '))
    if optexto == 1:
        maiusculo = texto.upper()
        print(f'Seu texto em maiúsculo é: {maiusculo}\n')
    elif optexto == 2:
        minusculo = texto.lower()
        print(f'Seu texto em minúsculo é: {minusculo}\n')
    elif optexto == 3:
        capit = texto.capitalize()
        print(f'Seu texto capitalizado é: {capit}')
    elif optexto == 4:
        title = texto.title()
        print(f'Seu texto com iniciais maiúsculas fica: {title}')
    elif optexto == 5:
        print('Finalizando...')
if op == 2:
    opmed = int(input('\nEscolha o que fazer:\n'
          '1. TEMPERATURA\n'
          '2. DISTÂNCIA\n'
          '3. TEMPO\n'
          '4. VOLUME\n'
          '5. SAIR\n'
          'Escolha uma opção: '))
    if opmed == 1:
        optemp = int(input('\nEscolha a temperatura inicial:\n'
                           '1. CELSIUS\n'
                           '2. FAHRENHEIT\n'
                           '3. KELVIN\n'
                           'Digite uma opção: '))
        temp = float(input('\nDigite a temperatura (°C / °F / K): '))
        cf = (temp * 9 / 5) + 32
        ck = temp + 273.15
        kc = temp - 273.15
        kf = (temp - 273.15) * 9/5 + 32
        fc = (temp - 32) * 5/9
        fk = (temp - 32) * 5/9 + 273.15
        if optemp == 1:
            print(f'A temperatura {temp}°C convertida é\nKelvin = {ck} K\nFahrenheit = {cf}°F')
        if optemp == 2:
            print(f'A temperatura {temp}°F convertida é\nCelsius = {fc}°C\nKelvin = {fk} K')
        if optemp == 3:
            print(f'A temperatura {temp} K convertida é\nCelsius = {kc}°C\nFahrenheit = {kf}°F')
    if opmed == 2:
        m = float(input('Digite a distância em metros: '))
        dm = m * 10
        cm = m * 100
        mm = m * 1000
        dc = m / 10
        hm = m / 100
        km = m / 1000
        print(f'O valor de {m}m equivale a \n'
                    f'{dm} Decímetros\n'
                    f'{cm} Centímetros\n'
                    f'{mm} Milímetros\n'
                    f'{dc} Decâmetros\n'
                    f'{hm} Hectômetros\n'
                    f'{km} Kilômetros\n')
    if opmed == 3:
        optempo1 = int(input('\nDigite a unidade que irá converter: \n'
                    '1. SEGUNDOS\n'
                    '2. MINUTOS\n'
                    '3. HORAS\n'
                    '4. DIA\n'
                    '5. SEMANA\n'
                    '6. MÊS\n'
                    '7. ANO\n'
                    'Escolha uma opção: '))
        optempo2 = int(input('\nDigite no que quer converter: \n'
                    '1. MINUTOS\n'
                    '2. HORAS\n'
                    '3. DIA\n'
                    '4. SEMANA\n'
                    '5. MÊS\n'
                    '6. ANO\n'
                    'Escolha uma opção: '))
        # SEGUNDOS
        # Segundos para Minuto
        if optempo1 == 1 and optempo2 == 1:
            segundos = float(input('Digite a quantia em SEGUNDOS: '))
            min = segundos / 60
            print(f'\n{segundos} segundos = {min:.2f} minutos')

        # Segundos para Hora
        if optempo1 == 1 and optempo2 == 2:
            segundos = float(input('Digite a quantia em SEGUNDOS: '))
            hrs = segundos / 3600
            print(f'\n{segundos} segundos = {hrs:.2f} horas')

        # Segundos para Dia
        if optempo1 == 1 and optempo2 == 3:
            segundos = float(input('Digite a quantia em SEGUNDOS: '))
            d = segundos / 86400
            print(f'\n{segundos} segundos = {d:.2f} dias')

        # Segundos para Semana
        if optempo1 == 1 and optempo2 == 4:
            segundos = float(input('Digite a quantia em SEGUNDOS: '))
            sem = segundos / 604800
            print(f'\n{segundos} segundos = {sem:.2f} semanas')

        # Segundos para Mês
        if optempo1 == 1 and optempo2 == 5:
            segundos = float(input('Digite a quantia em SEGUNDOS: '))
            m = segundos / 2592000

        # Segundos para Ano
        if optempo1 == 1 and optempo2 == 6:
            segundos = float(input('Digite a quantia em SEGUNDOS: '))
            a = segundos / 31536000
            print(f'\n{segundos} segundos = {a:.2f} ano(s)')

        # Minutos
        # Minutos para Hora
        if optempo1 == 2 and optempo2 == 2:
            minutos = float(input('Digite a quantia em MINUTOS: '))
            hrs = minutos / 60
            print(f'\n{minutos} minutos = {hrs:.2f} hora(s)')

        # Minutos para Dia
        if optempo1 == 2 and optempo2 == 3:
            minutos = float(input('Digite a quantia em MINUTOS: '))
            dia = minutos / 1440
            print(f'\n{minutos} minutos = {dia:.2f} dia(s)')

        # Minutos para Semana
        if optempo1 == 2 and optempo2 == 4:
            minutos = float(input('Digite a quantia em MINUTOS: '))
            semana = minutos / 10080
            print(f'\n{minutos} minutos = {semana:.2f} semana(s)')

        # Minutos para Mês
        if optempo1 == 2 and optempo2 == 5:
            minutos = float(input('Digite a quantia em MINUTOS: '))
            mes = minutos / 43800
            print(f'\n{minutos} minutos = {mes:.2f} mês(es)')

        # Minutos para Ano
        if optempo1 == 2 and optempo2 == 6:
            minutos = float(input('Digite a quantia em MINUTOS: '))
            ano = minutos / 525600
            print(f'\n{minutos} minutos = {ano:.2f} ano(s)')

        # Horas
        # Horas para Minuto
        if optempo1 == 3 and optempo2 == 1:
            horas = float(input('Digite a quantia em HORAS: '))
            minutos = horas / 60
            print(f'\n{horas} hora(s) = {minutos:.2f} minutos')

        # Horas para Hora
        if optempo1 == 3 and optempo2 == 2:
            horas = float(input('Digite a quantia em HORAS: '))
            horas = horas / 1
            print(f'\n{horas} hora(s) = {horas:.2f} hora(s)')

        # Horas para Dia
        if optempo1 == 3 and optempo2 == 3:
            horas = float(input('Digite a quantia em HORAS: '))
            dia = horas / 24
            print(f'\n{horas} horas = {dia:.2f} dia(s)')

        # Horas para Semana
        if optempo1 == 3 and optempo2 == 4:
            horas = float(input('Digite a quantia em HORAS: '))
            semana = horas / 168
            print(f'\n{horas} dias = {semana:.2f} semana(s)')

        # Horas para Mês
        if optempo1 == 3 and optempo2 == 5:
            horas = float(input('Digite a quantia em HORAS: '))
            mes = horas / 730
            print(f'\n{horas} dias = {mes:.2f} mês(es)')

        # Horas para Ano
        if optempo1 == 3 and optempo2 == 1:
            dias = float(input('Digite a quantia em DIAS: '))
            ano = dias / 8760
            print(f'\n{dias} dias = {ano:.2f} ano(s)')










if op == 3:
    mes = datetime.datetime.today().month
    ano = datetime.datetime.today().year
    print(f'NOTA: as contações são feitas em tempo-real\nPortanto, o ano é {ano} e o mês de número {mes} ')
    m = CurrencyRates()
    print('Conversor de moedas em tempo-real'
          '\nLista de moedas:'
          '\nBRL'
          '\nUSD...')
    moeda1 = input('Digite a primeira moeda: ').upper().strip()
    moeda2 = input('Em qual moeda ela será convertida? R:').upper().strip()
    quantia = int(input("Digite a quantia: "))
    print(moeda1, 'Para', moeda2, quantia)
    result = m.convert(moeda1, moeda2, quantia)
    print(result)
if op == 5:
    inicio = int(input('Em que número começar? R: '))
    final = int(input('E até onde vai? R: '))
    rand = randint(inicio, final)
    print(f'O intervalo vai de {inicio} até {final}.\nE o número aleatório foi {rand}.')
if op == 6:
    print('\nFinalizando...')
