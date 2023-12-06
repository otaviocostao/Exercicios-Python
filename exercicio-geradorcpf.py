nove_digitos= '345512323'
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
print(cpf_gerado)