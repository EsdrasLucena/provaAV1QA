import re

#Funcao de validacao de cpf

def validar_cpf(cpf: str) -> bool:
    """
    :param cpf: CPF como string (somente numeros ou no formato xxx.xxx.xxx-xx)
    :return: True se for valido, false caso contrario
    """
    cpf = re.sub(r'\D', '', cpf) #remove caracteres nao numericos

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False #cpf invalido se todos os numeros forem iguais

    #calculo do primeiro digito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma *10 % 11) %10

    #calculo do segundo digito verificador
    soma = sum(int(cpf[i]) * (11-i) for i in range (10))
    digito2 = (soma* 10 % 11) %10

    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])