from lexer import lexico
from parser import sintatico


data = """
    ++i;
    """

lexico.input(data)
for token in lexico:
    print(token)
result = sintatico.parse(data)
print(result)