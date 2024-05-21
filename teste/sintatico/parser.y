%{
// Seção de código entre %{ e %} é inserida diretamente no código C gerado
#include <stdio.h>
#include "y.tab.h"
extern char *yytext;  // Declaração externa de yytext para uso em y.tab.c
int yylex(void);      // Função gerada por Flex para análise léxica
int yyerror(const char *s);  // Função chamada em caso de erro de análise
%}

// Declaração dos tokens utilizados pelo analisador léxico e sintático
%token ADD SUB MUL DIV NUMBER LPAREN RPAREN

%%

// Regras de produção para a gramática da linguagem
expression:
    expression ADD term
    | expression SUB term
    | term
    ;

term:
    term MUL factor
    | term DIV factor
    | factor
    ;

factor:
    NUMBER
    | LPAREN expression RPAREN
    ;

%%

// Função principal
int main() {
    yyparse();  // Chamada da função principal de análise sintática
    return 0;
}

// Função chamada em caso de erro de análise
int yyerror(const char *s) {
    fprintf(stderr, "Erro de análise: %s\n", s);
    fprintf(stderr, "Último token lido: %s\n", yytext);
    fprintf(stderr, "Local do erro: %s\n", yytext);
    return 0;
}

// Função chamada para indicar o fim do arquivo durante a análise léxica
int yywrap(void) {
    return 1;
}