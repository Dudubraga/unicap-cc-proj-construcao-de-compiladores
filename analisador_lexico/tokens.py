palavras_reservadas = ["int", "float", "char", "boolean", "while", "for", "main", "return", "if", "else", "void", "println", "String","static","public", "class", "System", "out", "in"]

operadores = ["=", "+", "-", "/", "*", "%", "&&", "||", "!"]

comparacao = [">", ">=", "<", "<=", "==", "!="]

simbolos_especiais = ["(", ")", ",", "[", "]", ";", "{", "}" , ".", "#"]

identificadores = []
lista_tokens = []
NUM_INT = []
NUM_DEC = []
const_txt = []

# funcoes : isnumeric() , readlines() , open()
npt = '/home/henriquefranca/github/compiladores/codigo_fonte.txt'

arquivo = 'codigo_fonte.txt'
index = 1
comentario = False
try:
    with open(arquivo,'r') as codigo:
        linhas = codigo.readlines()
        linhas = [linha.strip() for linha in linhas]
except FileNotFoundError:
    print(f"Arquivo {arquivo} não encontrado!")

for s in linhas:
    while len(s) != 0:
        current = str(s[0]) # string recebe o primeiro caractér de s 
        s = s[1:] # o primeiro caractér é removido de s
        # IF para reconhecer Números Inteiros e Decimais
        if current.isnumeric() and not comentario: 
            while s[0].isnumeric() or s[0] == '.':
                current += str(s[0])
                s = s[1:]
            if '.' in current:
                NUM_DEC.append(current)
                lista_tokens.append("NUM_DEC")
                print("NUM_DEC (" + current + ")")
            else:
                NUM_INT.append(current)
                lista_tokens.append("NUM_INT")
                print("NUM_INT (" + current + ")")

        
        # IF para reconhecer Simbolos Especiais
        elif current in simbolos_especiais and not comentario: 
            lista_tokens.append(current)
            print(current)

        # IF para reconhecer Strings
        elif current == '"' and not comentario: 
            while s[0] != '"':
                current += s[0]
                s = s[1:]
            current += s[0]
            s = s[1:]
            const_txt.append(current)
            lista_tokens.append("const_TXT")
            print("const_TXT (" + current + ")")
                        
        # IF para reconhecer Comparadores 
        elif current in comparacao or (len(s) > 0 and (current + s[0] == "==" or current + s[0] == "!=") and not comentario): 
            if current + s[0] == "==" or current + s[0] == "!=":
                current += s[0]
                s = s[1:]
            if (current == '<' or current == '>') and s[0] == "=":
                current += s[0]
                s = s[1:]
            lista_tokens.append(current)
            print(current)

        # IF para reconhecer Comentário em Linha
        elif (current == '/' and s[0] == '/') and not comentario:
            break
        # IF para reconhecer o ínicio do Comentário Com Várias Linhas
        elif current == "/" and s[0] == "*":
            comentario = True
            s = s[1:]          
        # IF para reconhecer o fim do Comentário de Várias Linhas
        elif current == "*" and s[0] == "/":
            comentario = False
            s = s[1:]

        # IF para reconhecer Operadores
        elif current in operadores and not comentario: 
            if (current == '&' or current == '|') and current == s[0]:
                current = current + s[0]
                s = s[1:]
            lista_tokens.append(current)
            print(current)
                
        # IF para reconhecer Palavras Reservadas e IDs de variáveis
        elif current != " " and not comentario: 
            while len(s) > 0 and (s[0] not in operadores) and (s[0] not in comparacao) and (s[0] not in simbolos_especiais) and s[0] != ' ':
                current += str(s[0])
                s = s[1:]
            if current in palavras_reservadas:
                lista_tokens.append(current)
                print(current)
            else:
                if current not in identificadores:
                    identificadores.append(current)
                    lista_tokens.append("id, " + str(index))
                    print("id, " + str(index) + " (" + current + ")")
                    index += 1
                else:
                    lista_tokens.append("id, " + str(identificadores.index(current)+1))
                    print("id, " + str(identificadores.index(current)+1) + " (" + current + ")")
