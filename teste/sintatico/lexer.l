%{
#include <stdio.h>
#include "y.tab.h"

%}

%%

[0-9]+      { yylval = atoi(yytext); return NUMBER; }
[-+*/()\n]  { return yytext[0]; }
[ \t]       ; // Ignora espaços em branco e tabulações
.           { 
                fprintf(stderr, "Caractere desconhecido: %s\n", yytext);
                yyerror("Erro léxico"); // Adiciona uma chamada a yyerror para relatar o erro
            }

%%
