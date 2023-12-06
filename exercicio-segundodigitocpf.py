"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""

cpf = '746.824.890-70'.replace('.', '').replace('-', '').replace(' ', '')
nove_digitos= cpf[:9]
contador_regressivo = 10
contador_regressivo_1 = 11
soma_digitos = 0
soma_digitos_1 = 0

for digito in nove_digitos:
    soma_digitos += int(digito) * contador_regressivo
    contador_regressivo -= 1

primeiro_digito = (soma_digitos*10)%11

primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

dez_digitos = nove_digitos + str(primeiro_digito)
for digito_1 in dez_digitos:
    soma_digitos_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1

segundo_digito = (soma_digitos_1*10)%11

segundo_digito = segundo_digito if segundo_digito <=9 else 0

cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if cpf == cpf_gerado:
    print(f'O CPF: {cpf} enviado pelo usuário é valido')
else:
    print(f'O CPF: {cpf} inviado pelo usuário é invalido')