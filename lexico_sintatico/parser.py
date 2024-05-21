from ply import yacc
from lexer import tokens

def p_programa(p):
    """
    programa : declaracao
    """

def p_declaracao(p):
    """
    declaracao : declaracao_variavel
                | declaracao_funcao
                | declaracao_estrutura
                | comentario
    """

def p_declaracao_variavel(p):
    """
    declaracao_variavel : tipo ID SEMICOLON
                        | tipo ID = expressao SEMICOLON
    """
    
def p_tipo(p):
    """
    tipo : int
         | float
         | double
         | char
         | boolean
    """

def p_declaracao_funcao(p):
    """
    declaracao_funcao : tipo ID LPAREN parametros RPAREN bloco
    """

def p_parametros(p):
    """
    parametros : parametro
               | parametro COMMA parametro
               | tipo ID
               | tipo ID LBRACKET RBRACKET
    """

def p_bloco(p):
    """
    bloco : LBRACE declaracao RBRACE

    """
    
def p_comentario(p):
    """

    """

def p_expressoes(p):
    """
    expressoes : atribuicao
    """

def p_atribuicao(p):
    """
    atribuicao : ID EQUAL expressao
               | ID PLUSEQUAL expressao
               | ID MINUSEQUAL expressao
               | ID TIMESEQUAL expressao
               | ID DIVEQUAL expressao
               | ID MODEQUAL expressao
               | ID ANDANDEQUAL expressao
               | ID OROREQUAL expressao
               | ID EQUAL ID
               | ID PLUSEQUAL ID
               | ID MINUSEQUAL ID
               | ID TIMESEQUAL ID
               | ID DIVEQUAL ID
               | ID MODEQUAL ID
               | ID ANDANDEQUAL ID
               | ID OROREQUAL ID
    """
    
def p_estrutura_controle(p):
    """
    estrutura_controle : IF LPAREN expressao RPAREN 
    """

def p_declaracao_estrutura(p):
    """
    declaracao_estrutura : struct ID { declaracao_variavel }
    """
    
def p_array(p):
    """
    array : ID [ expressao ]
          | ID [ ]
          | ID { expressao_lista }
    """

def p_expressao(p):
    """
    expressao : expressao_logica
    """
    
def p_expressao_logica(p):
    """
    expressao_logica : expressao_relacional
                     | expressao_logica && expressao_relacional
                     | expressao_logica || expressao_relacional
    """

def p_expressao_relacional(p):
    """
    expressao_relacional : expressao_aritmetica
                         | expressao_aritmetica >
                         | expressao_aritmetica >=
                         | expressao_aritmetica <
                         | expressao_aritmetica <=
                         | expressao_aritmetica !=
                         | expressao_aritmetica ==
    """

def p_expressao_aritmetica(p):
    """
    expressao_aritmetica : expressao_multiplicativa
                         | expressao_aritmetica + expressao_multiplicativa
                         | expressao_aritmetica - expressao_multiplicativa
    """

def p_expressao_multiplicativa(p):
    """
    expressao_multiplicativa : expressao_unaria
                             | expressao_multiplicativa * expressao_unaria
                             | expressao_multiplicativa / expressao_unaria
                             | expressao_multiplicativa % expressao_unaria
    """

def p_expressao_unaria(p):
    """
    expressao_unaria : expressao_postfix
                     | -expressao_unaria
                     | ++ expressao_postfix
                     | -- expressao_postfix
    """

def p_expressao_postfix(p):
    """
    expressao_postfix : primaria
                      | primaria [ expressao ]
                      | primaria ( argumentos )
                      | primaria . ID
    """

def p_argumentos(p):
    """
    argumentos : expressao_lista
               | 
    """

def p_primaria(p):
    """
    primaria : ID
             | NUM_INT
             | NUM_DEC
             | TEXTO
             | ( expressao )
    """