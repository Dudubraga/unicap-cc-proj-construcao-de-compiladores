%{
#include <stdio.h>
#include <stdlib.h>
extern int yylex();
void yyerror(const char *s);
%}

%token INT FLOAT DOUBLE CHAR BOOLEAN STRUCT
%token IF ELSE WHILE FOR SWITCH CASE DEFAULT
%token BREAK CONTINUE RETURN
%token NUM_INT NUM_DEC TEXTO ID

%%

programa : /* empty */
         | programa declaracao
         ;

declaracao : declaracaoVariavel
           | declaracaoFuncao
           | declaracaoEstrutura
           | comentario
           ;

declaracaoVariavel : tipo ID ';'
                   | tipo ID '=' expressao ';'
                   ;

tipo : INT
     | FLOAT
     | DOUBLE
     | CHAR
     | BOOLEAN
     ;

declaracaoFuncao : tipo ID '(' parametros ')' bloco
                 ;

parametros : /* empty */
           | parametro
           | parametros ',' parametro
           ;

parametro : tipo ID
          | tipo ID '[]'
          | tipo ID '...'
          ;

bloco : '{' declaracoes '}'
      ;

declaracoes : /* empty */
            | declaracoes declaracao
            ;

comentario : /* empty */
           ;

/* ... Restante das regras ... */

%%

void yyerror(const char *s) {
  fprintf(stderr, "Erro de análise: %s\n", s);
}

int main(void) {
  return yyparse();
}
