
inteiros = {}
flutuantes = {}
booleanos = {}
operadores = {'+', '-', '*', '/'}

data = """
    
    int x = 10;
    float z = 9.0;
    int h = 12.23;
    
    2 + 3 * 2;

    """
lista = data.split('\n')

for l in lista:
    while len(lista) != 0:
        current = str(l[0])
        l = l[1:] #remove o primeiro caracter de l
        for i in range(len(lista)):
            if l[0] == ' ':
                l = l[1:]
                break;    
            current += l[i]
            l = l[1:]

        tipo = '0'
        if current == 'int':
            tipo = 'int'
        elif current == 'float':
            tipo = 'float'
        elif current == 'double':    
            tipo = 'double'
        elif current == 'boolean':    
            tipo = 'boolean'
        current = ''

        while l[0] != ' ':
            current += l[0]
            l = l[1:]
        l = l[1:]
        if tipo != '0' and current in (inteiros or flutuantes or booleanos): 
            print(f'variável {current} declarada novamente')
            exit()
        elif tipo == '0' and not (current in (inteiros or flutuantes or booleanos)):
            print(f'variavel {current} não declarada')
            exit()
        elif tipo == 'float' or tipo == 'double':
            flutuantes.append(current)

        elif tipo == 'int':
            inteiros.append(current)
        
        elif tipo == 'boolean':
            booleanos.append(current)
        
        print(f"váriavel {current}, TIPO: {tipo}")

        current = ''
        current += l[0]
        l = l[1:]

        if current == ';':
            break
        elif current == '=':
            current = ''
            l = l[1:]
            while l[0] != ' ':
                current += l[0]
                l = l[1:]
            l = l[1:]
            if current == 'True' or current == 'False':
                tipo = 'boolean'
            elif '.' in current:
                tipo = 'float'
            else:
                tipo = 'int'
        elif current in operadores:
            break

