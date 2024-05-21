from ply import lex

# Lista de tokens
tokens = (
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'ID', 'EQUALS',
    'TIPO', 'SEMICOLON', 'LBRACE', 'RBRACE',
    'COMMA', 'COMMENT', 'LBRACKET', 'RBRACKET',
    'DOTDOTDOT', 'OROR', 'ANDAND', 'NOT',
    'GREATER', 'LESS', 'GREATEREQUAL', 'LESSEQUAL',
    'NOTEQUAL', 'EQUAL', 'MODULO', 'DOT',
    'ARROW', 'NUM_INT', 'NUM_DEC', 'TEXTO',
    'PLUSEQUAL', 'MINUSEQUAL', 'TIMESEQUAL', 'DIVEQUAL',
    'MODEQUAL', 'ANDANDEQUAL', 'OROREQUAL', 
)

# Regras para cada token
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_SEMICOLON = r';'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_COMMA = r','
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_DOTDOTDOT = r'\.\.\.'
t_OROR = r'\|\|'
t_ANDAND = r'&&'
t_NOT = r'!'
t_GREATER = r'>'
t_LESS = r'<'
t_GREATEREQUAL = r'>='
t_LESSEQUAL = r'<='
t_NOTEQUAL = r'!='
t_EQUAL = r'=='
t_MODULO = r'%'
t_DOT = r'.'
t_ARROW = r'->'
t_PLUSEQUAL = r'\+='
t_MINUSEQUAL = r'-='
t_TIMESEQUAL = r'\*='
t_DIVEQUAL = r'/='
t_MODEQUAL = r'%='
t_ANDANDEQUAL = r'&&='
t_OROREQUAL = r'\|\|='

# Regra para tipo
def t_TIPO(t):
    r'int|float|double|char|boolean'
    t.value = str(t.value)
    return t

# Regra para números
def t_NUM_DEC(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUM_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regra para id
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.value = str(t.value)
    return t

# Expressão regular para comentários/texto
def t_COMMENT(t):
    r'//.*'
    return t

def t_TEXTO(t):
    r'\"[^\"]*\"'
    t.value = t.value[1:-1]  # Remover as aspas da string
    return t

# Ignorar caracteres em branco
t_ignore = ' \t\n'

# Manipulador de erros
def t_error(t):
    print(f"Caractere inesperado na linha : {t.value[0]}")
    t.lexer.skip(1)

# Criar o analisador léxico
lexer = lex.lex()