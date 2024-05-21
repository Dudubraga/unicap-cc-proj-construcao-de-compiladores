from ply import yacc
from lexer import tokens
ln = 0

def linha():
    global ln
    ln += 1

# Regras de produção
def p_programa(p):
    """
    programa : declaracao
            | declaracao programa
    """

def p_declaracao(p):
    """
    declaracao : declaracaoVariavel
                | declaracaoFuncao
                | declaracaoEstrutura
                | comentario
    """

def p_declaracaoVariavel(p):
    """
    declaracaoVariavel : TIPO ID SEMICOLON
                        | TIPO ID EQUALS expressao SEMICOLON
                        | TIPO array SEMICOLON
                        | TIPO array EQUALS TEXTO SEMICOLON
    """

def p_array(p):
    """array : ID LBRACKET RBRACKET"""

def p_declaracaoFuncao(p):
    """
    declaracaoFuncao : TIPO ID LPAREN parametros RPAREN bloco
    """

def p_parametros(p):
    """
    parametros : parametro
                | parametro COMMA parametros
    """

def p_parametro(p):
    """
        parametro : TIPO ID
                | TIPO ID LBRACKET RBRACKET
                | TIPO DOTDOTDOT ID
    """

def p_comentario(p):
    """
    comentario : COMMENT
    """

def p_bloco(p):
    """
    bloco : LBRACE declaracao RBRACE
    """

def p_declaracaoEstrutura(p):
    """
    declaracaoEstrutura : LBRACE declaracaoVariavel RBRACE SEMICOLON
    """

def p_expressaoLogica(p):
    """
    expressaoLogica : expressaoRelacional
                    | expressaoLogica OROR expressaoRelacional
                    | expressaoLogica ANDAND expressaoRelacional
                    | NOT expressaoRelacional
    """

def p_expressaoRelacional(p):
    """
    expressaoRelacional : expressaoAritmetica
                        | expressaoAritmetica GREATER expressaoAritmetica
                        | expressaoAritmetica LESS expressaoAritmetica
                        | expressaoAritmetica GREATEREQUAL expressaoAritmetica
                        | expressaoAritmetica LESSEQUAL expressaoAritmetica
                        | expressaoAritmetica NOTEQUAL expressaoAritmetica
                        | expressaoAritmetica EQUAL expressaoAritmetica
    """

def p_expressao(p):
    """
    expressao : expressaoLogica
            | atribuicao
    """

def p_atribuicao(p):
    """
        atribuicao : ID EQUALS expressao
                    | ID PLUSEQUAL expressao
                    | ID MINUSEQUAL expressao
                    | ID TIMESEQUAL expressao
                    | ID DIVEQUAL expressao
                    | ID MODEQUAL expressao
                    | ID ANDANDEQUAL expressao
                    | ID OROREQUAL expressao
    """

def p_expressaoAritmetica(p):
    """
    expressaoAritmetica : expressaoMultiplicativa
                        | expressaoAritmetica PLUS expressaoMultiplicativa
                        | expressaoAritmetica MINUS expressaoMultiplicativa
    """

def p_expressaoMultiplicativa(p):
    """
    expressaoMultiplicativa : expressaoMultiplicativa TIMES expressaoUnaria
                            | expressaoMultiplicativa DIVIDE expressaoUnaria
                            | expressaoMultiplicativa MODULO expressaoUnaria
                            | expressaoUnaria

    """

def p_expressaoUnaria(p):
    """
    expressaoUnaria : expressaoPostfix
                    | MINUS expressaoPostfix
                    | PLUS PLUS expressaoPostfix
                    | MINUS MINUS expressaoPostfix
    """

def p_expressaoPostfix(p):
    """
    expressaoPostfix : primaria
                    | primaria LBRACKET expressao RBRACKET
                    | primaria LPAREN argumentos RPAREN
                    | primaria DOT ID
                    | primaria ARROW ID
    """

def p_argumentos(p):
    """
    argumentos :
    """

def p_primaria(p):
    """
    primaria : ID
            | NUM_INT
            | NUM_DEC
            | LPAREN expressao LPAREN
            | TEXTO
    """

# Manipulador de erros
def p_error(p):
    global ln
    print(f"Erro de sintaxe na linha {ln}")

# Criar o analisador sintático
parser = yacc.yacc()