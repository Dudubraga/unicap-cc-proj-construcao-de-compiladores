# Compiladores
Construção de compiladores

A primeira fase deste projeto é a implementação do Analisador Léxico. Este componente é fundamental para a estruturação do compilador, sendo responsável por ler os caracteres do código-fonte, agrupá-los em lexemas e produzir uma sequência de tokens. Estes tokens são identificados com base em padrões definidos por expressões regulares e são categorizados para facilitar as fases subsequentes do processo de compilação.
Para o projeto em questão, o analisador léxico deve reconhecer um conjunto específico de tokens, conforme o alfabeto definido:

- Números Inteiros (NUM_INT): Sequências de dígitos, como "123".
- Números Decimais (NUM_DEC): Números com parte decimal, como "123.456".
- Identificadores (ID): Sequências que começam com uma letra ou sublinhado, seguidas por letras, dígitos ou sublinhados.
- Constantes de Texto (TEXTO): Sequências de caracteres entre aspas duplas.
- Palavras Reservadas: São palavras específicas da linguagem, como "int", "float", "char", "boolean", "void", "if", "else", "for", "while", "scanf", "println", "main" e "return".
- Comentários: Sequências que começam com "//" e continuam até o final da linha.
- Operadores: São símbolos que representam operações, como "=", "+", "-", "*", "/", "%", "&&", "||", "!" e operadores de comparação como ">", ">=", "<", "<=", "!=", "==".
- Símbolos Especiais: São caracteres que têm significados especiais na linguagem, como "(", ")", "[", "]", "{", "}", ",", ";".

O analisador léxico deve ser capaz de identificar e categorizar cada token com base nas expressões regulares fornecidas, garantindo que o código-fonte esteja em conformidade com o alfabeto definido. Ao encontrar um lexema que não corresponda a nenhum padrão, o analisador deve gerar um erro, indicando que o código-fonte contém um token inválido. Esta é a primeira etapa do projeto.
