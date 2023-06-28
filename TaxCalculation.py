import os
from pathlib import Path
import locale

PATH_ARQUIVE = Path(__file__).parent / 'result.txt'


def convert_float(value):
    try:
        value = value.replace(',', '.')
        return float(value)
    except ValueError:
        print('Digite um número válido') 

def convert_int(value):
    try:
        return int(value)
    except ValueError:
        print('Digite um número Inteiro')   


def convert_percent(value):
    return value/100 + 1


def mandar_json(cod, quantity, result):

    with open(PATH_ARQUIVE, 'a', encoding='utf8') as arquive:

        # locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
        # resultado = locale.currency(resultado, grouping=True, symbol=True)
        formattedMessaged = f'{cod} ------- {quantity} ------- R$ {resultado:.2f}'
        arquive.write(formattedMessaged)
        arquive.write('\n')



valueST = convert_float(input('\nDigite o Valor ST: R$ '))

allProductsValue = convert_float(input('\nDigite o Valor dos Produtos: R$ '))

delivery = round(convert_float(input('\nFrete: ')), 2)

spotPrice = round(convert_float(input('\nÀ vista: ')), 2)

percentST = round(((valueST * 100) / allProductsValue),2)

while True:
    os.system('cls')
    print('ST:',percentST, '%')

    cod = input('\nCódigo: ')
    quantity = convert_int(input('\nQuantidade: '))
    totalValue = convert_float(input('\nValor: R$ '))
    ipi = convert_float(input('\nIPI: R$ '))

   
    resultado = (totalValue * convert_percent(percentST)) + ipi

    if not delivery == 0:
        resultado *= convert_percent(delivery)

    if not spotPrice == 0:
        resultado *= convert_percent(spotPrice)
        
    if not quantity == 1:
        resultado /= quantity

    os.system('cls')
    print(f'Código: {cod}')
    print(f'Quantidade: {quantity}')
    print(f'Valor Total: R$ {totalValue:.2f}')
    print(f'IPI: R$ {ipi:.2f}')
    print()
    print(f'Resultado: R$ {resultado}')
    confirmar_usuario = input('\nRetornar ? [s]: ')

    if confirmar_usuario.lower() == 's':
        continue
    else:
        mandar_json(cod, quantity, resultado) 
