from lexer import lexico
from parser import sintatico


data = """
    int main(){
        int a;
        a = 10;
        return 0;
    }
    """

lexico.input(data)
for token in lexico:
    print(token)
result = sintatico.parse(data)
print(result)