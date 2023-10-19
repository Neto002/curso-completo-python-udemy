import re
import random

def trata_cpf(cpf: str) -> str:
    return re.sub(r'[^0-9]', '', cpf)

def calcula_primeiro_digito_cpf(cpf: str) -> str:
    cpf = trata_cpf(cpf)
    nove_digitos = cpf[:9]
    multiplicador = 10
    resultado = 0

    for digito in nove_digitos:
        resultado += int(digito) * multiplicador
        multiplicador -= 1

    primeiro_digito = (resultado * 10) % 11
    return "0" if primeiro_digito > 9 else str(primeiro_digito)

def calcula_segundo_digito_cpf(cpf: str) -> str:
    cpf = trata_cpf(cpf)
    primeiro_digito = calcula_primeiro_digito_cpf(cpf)
    multiplicador = 11
    resultado = 0

    for digito in cpf[:9] + str(primeiro_digito):
        resultado += int(digito) * multiplicador
        multiplicador -= 1

    segundo_digito = (resultado * 10) % 11
    return "0" if segundo_digito > 9 else str(segundo_digito)

def gerar_cpf() -> str:
    nove_digitos = ''.join([str(random.randint(0, 9)) for _ in range(0, 9)])
    return f'{nove_digitos}{calcula_primeiro_digito_cpf(nove_digitos)}{calcula_segundo_digito_cpf(nove_digitos)}'

def valida_cpf(cpf: str) -> bool:  
    cpf = trata_cpf(cpf)
    if (len(cpf) != 11):
        return False
    entrada_sequencial = cpf == cpf[0] * len(cpf)
    if (entrada_sequencial):
        return False
    primeiro_digito = calcula_primeiro_digito_cpf(cpf)
    segundo_digito = calcula_segundo_digito_cpf(cpf)

    cpf_gerado = f'{cpf[:9]}{primeiro_digito}{segundo_digito}'

    return True if cpf == cpf_gerado else False

print(valida_cpf(gerar_cpf()))