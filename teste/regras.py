def Regra():
    lista_regras = {'Programa': [], 'Declaracao': [], 'DeclaracaoVariavel': [], 'Tipo': [], 'DeclaracaoFuncao': [],
                 'Parametros': [], 'Bloco': [], 'Comentario': [], 'Expressoes': [], 'Atribuicao': [],
                 'EstruturaControle': [], 'DeclaracaoEstrutura': [], 'Array': [], 'Expressao': [],
                 'ExpressaoLogica': [], 'ExpressaoRelacional': [], 'ExpressaoAritmetica': [],
                 'ExpressaoMultiplicativa': [], 'ExpressaoUnaria': [], 'ExpressaoPostfix': [], 'Argumentos': [],
                 'Primaria': []}

    lista_regras['Programa'].append('Declaracao')

    lista_regras['Declaracao'].append('DeclaracaoVariavel')
    lista_regras['Declaracao'].append('DeclaracaoFuncao')
    lista_regras['Declaracao'].append('DeclaracaoEstrutura')
    lista_regras['Declaracao'].append('Comentario')

    lista_regras['DeclaracaoVariavel'].append('Tipo ID')
    lista_regras['DeclaracaoVariavel'].append('Tipo ID = Expressao')

    lista_regras['Tipo'].append('int')
    lista_regras['Tipo'].append('float')
    lista_regras['Tipo'].append('double')
    lista_regras['Tipo'].append('char')
    lista_regras['Tipo'].append('boolean')

    lista_regras['DeclaracaoFuncao'].append('Tipo ID ( Parametros ) Bloco')

    lista_regras['Parametros'].append('Parametro')
    lista_regras['Parametros'].append('Parametro, Parametros')
    lista_regras['Parametros'].append('Tipo ID')
    lista_regras['Parametros'].append('Tipo ID []')
    lista_regras['Parametros'].append('Tipo ... ID')

    lista_regras['Bloco'].append('{ Declaracao }')

    lista_regras['Comentario'].append('// Qualquer texto ate o final da linha')
    lista_regras['Comentario'].append('/* Qualquer texto ate */')

    lista_regras['Expressoes'].append('Atribuicao')

    lista_regras['Atribuicao'].append('D = Expressao')
    lista_regras['Atribuicao'].append('ID += Expressao')
    lista_regras['Atribuicao'].append('ID -= Expressao')
    lista_regras['Atribuicao'].append('ID *= Expressao')
    lista_regras['Atribuicao'].append('ID /= Expressao')
    lista_regras['Atribuicao'].append('D %= Expressao')
    lista_regras['Atribuicao'].append('ID &&= Expressao')
    lista_regras['Atribuicao'].append(' ID ||= Expressao')
    lista_regras['Atribuicao'].append('ID = ID')
    lista_regras['Atribuicao'].append('ID += ID')
    lista_regras['Atribuicao'].append('ID -= ID')
    lista_regras['Atribuicao'].append('ID *= ID')
    lista_regras['Atribuicao'].append('ID /= ID')
    lista_regras['Atribuicao'].append('D %= ID')
    lista_regras['Atribuicao'].append('ID &&= ID')
    lista_regras['Atribuicao'].append('ID ||= ID')

    lista_regras['EstruturaControle'].append('if ( Expressao ) Bloco')
    lista_regras['EstruturaControle'].append('if ( Expressao ) Bloco else Bloco')
    lista_regras['EstruturaControle'].append('while ( Expressao ) Bloco')
    lista_regras['EstruturaControle'].append('for ( Expressao ; Expressao ; Expressao ) Bloco')
    lista_regras['EstruturaControle'].append('switch ( Expressao ) CaseLista')
    lista_regras['EstruturaControle'].append('CaseDecl')
    lista_regras['EstruturaControle'].append('case Expressao : Bloco')
    lista_regras['EstruturaControle'].append('break ;')
    lista_regras['EstruturaControle'].append('continue ;')
    lista_regras['EstruturaControle'].append('return Expressao ;')

    lista_regras['DeclaracaoEstrutura'].append('struct ID { DeclaracaoVariavel }')

    lista_regras['Array'].append('ID [ Expressao ]')
    lista_regras['Array'].append('ID [ ]')
    lista_regras['Array'].append('{ ExpressaoLista }')

    lista_regras['Expressao'].append('ExpressaoLogica')

    lista_regras['ExpressaoLogica'].append('ExpressaoRelacional')
    lista_regras['ExpressaoLogica'].append('ExpressaoLogica && ExpressaoRelacional')
    lista_regras['ExpressaoLogica'].append('ExpressaoLogica || ExpressaoRelacional')
    lista_regras['ExpressaoLogica'].append('! ExpressaoRelacional')

    lista_regras['ExpressaoRelacional'].append('ExpressaoAritmetica')
    lista_regras['ExpressaoRelacional'].append('ExpressaoAritmetica > ExpressaoAritmetica')
    lista_regras['ExpressaoRelacional'].append('ExpressaoAritmetica >= ExpressaoAritmetica')
    lista_regras['ExpressaoRelacional'].append('ExpressaoAritmetica < ExpressaoAritmetica')
    lista_regras['ExpressaoRelacional'].append('ExpressaoAritmetica <= ExpressaoAritmetica')
    lista_regras['ExpressaoRelacional'].append('ExpressaoAritmetica != ExpressaoAritmetica')
    lista_regras['ExpressaoRelacional'].append('ExpressaoAritmetica == ExpressaoAritmetica')

    lista_regras['ExpressaoAritmetica'].append('ExpressaoMultiplicativa')
    lista_regras['ExpressaoAritmetica'].append('ExpressaoAritmetica + ExpressaoMultiplicativa')
    lista_regras['ExpressaoAritmetica'].append('ExpressaoAritmetica - ExpressaoMultiplicativa')

    lista_regras['ExpressaoMultiplicativa'].append('ExpressaoUnaria')
    lista_regras['ExpressaoMultiplicativa'].append('ExpressaoMultiplicativa * ExpressaoUnaria')
    lista_regras['ExpressaoMultiplicativa'].append('ExpressaoMultiplicativa / ExpressaoUnaria')
    lista_regras['ExpressaoMultiplicativa'].append('ExpressaoMultiplicativa % ExpressaoUnaria')

    lista_regras['ExpressaoUnaria'].append('ExpressaoPostfix')
    lista_regras['ExpressaoUnaria'].append('-ExpressaoUnaria')
    lista_regras['ExpressaoUnaria'].append('++ ExpressaoPostfix')
    lista_regras['ExpressaoUnaria'].append('-- ExpressaoPostfix')

    lista_regras['ExpressaoPostfix'].append('Primaria')
    lista_regras['ExpressaoPostfix'].append('Primaria [ Expressao ]')
    lista_regras['ExpressaoPostfix'].append('Primaria ( Argumentos )')
    lista_regras['ExpressaoPostfix'].append('Primaria . ID')
    lista_regras['ExpressaoPostfix'].append('Primaria -> ID')

    lista_regras['Argumentos'].append('ExpressaoLista')
    lista_regras['Argumentos'].append('vazio')

    lista_regras['Primaria'].append('ID')
    lista_regras['Primaria'].append('NUM_INT')
    lista_regras['Primaria'].append('NUM_DEC')
    lista_regras['Primaria'].append('TEXTO')
    lista_regras['Primaria'].append('( Expressao )')

    return lista_regras