palavras_reservadas = ["int", "float", "while", "for", "char", "main", "return", 
                        "boolean", "if", "else", "void", "println","String",]

operadores = ["=", "+", "-", "/", "*", "%", "&&", "||", "!"]

operadores_comparacao = [">", ">=", "<", "<=", "==", "!="]

simbolos_especiais = ["(", ")", ",", "[", "]", "{", "}", ";"]

identificadores = []
lista_tokens = []
NUM_INT = []
NUM_DEC = []
const_txt = []

# funcoes : isnumeric() , readlines() , open()
arquivo = "codigo_fonte.txt"

def analisador_lexico():
    try:
        with open(arquivo,'r') as codigo:
            linhas = codigo.readlines()
            linhas = [linha.strip() for linha in linhas]
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado!")
    
    


