import semantico as semantico
from lexer import lexico
from parser import sintatico


def compilador():
    data = '''
        float a; 
        a = 2;
        int b;
        b = 1;
        boolean validate;
        validate = True;
        float d; 
        d = (2+2)/2;
    '''
    lista = data.split('\n')

    lexico.input(data)
    for token in lexico:
        print(token)

    result = sintatico.parse(data)

    print(result)
    
    if semantico.analisar(data):
        print("Análise semântica feito com sucesso!")

if __name__ == "__main__":
    compilador()
