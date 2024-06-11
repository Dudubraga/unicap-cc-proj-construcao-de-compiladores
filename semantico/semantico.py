class Variavel:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

variaveis = []

def add_variavel(nome, tipo):
    variaveis.append(Variavel(nome, tipo))

def verificar_variavel(nome):
    for variavel in variaveis:
        if variavel.nome == nome:
            return True
    return False

def ver_atribuicao(tipo1, tipo2):
    if tipo1 == 'int' and tipo2 == 'float':
        return False
    if tipo1 == 'boolean' and (tipo2 == 'float' or tipo2 == 'int'):
        return False
    if (tipo1 == 'float' or tipo2 == 'int') and tipo2 == 'boolean':
        return False
    
    return True

def get_tipo(nome):
    for variavel in variaveis:
        if variavel.nome == nome:
            return variavel.tipo
    return None

def analisar(data):
    linhas = data.split('\n')
    for i, linha in enumerate(linhas):
        if 'int ' in linha or 'float ' in linha or 'boolean' in linha:
            l = linha.split()
            tipo = l[0]
            nome = l[1].replace(';', '')
            add_variavel(nome, tipo)
        elif '=' in linha:
            l = linha.split('=')
            variavel = l[0].strip()
            valor = l[1].strip().replace(';', '')
            if not verificar_variavel(variavel):
                print(f"Erro semântico: variável '{variavel}' não declarada na linha {i+1}")
                return False
            tipo_variavel = get_tipo(variavel)
            if valor.isdigit():
                tipo_valor = 'int'
            elif valor.replace('.', '', 0).isdigit():
                tipo_valor = 'float'
            elif valor == 'True' or valor == 'False':
                tipo_valor = 'boolean'
            else:
                tipo_valor = 'expressao'
            
            if not ver_atribuicao(tipo_variavel, tipo_valor):
                print(f"Erro semântico: atribuição de tipo incompatível para a variável '{variavel}' na linha {i+1}")
                return False
    return True
