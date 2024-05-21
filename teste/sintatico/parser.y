%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void yyerror(const char *s);
int yylex();
%}

%union {
    int ival;
    double dval;
    char *sval;
}

%token <ival> NUM_INT
%token <dval> NUM_DEC
%token <sval> STRING
%token <sval> IDENTIFIER
%token INT FLOAT DOUBLE CHAR BOOLEAN
%token IF ELSE WHILE FOR SWITCH CASE DEFAULT BREAK CONTINUE RETURN STRUCT
%token AND OR NOT EQ NEQ GE LE GT LT
%token PLUS MINUS TIMES DIVIDE MOD ASSIGN
%token LPAREN RPAREN LBRACE RBRACE LBRACKET RBRACKET SEMICOLON COMMA DOT ARROW

%%

program:
    declaration_list
;

declaration_list:
    declaration_list declaration
    | /* empty */
;

declaration:
    variable_declaration
    | function_declaration
    | struct_declaration
    | comment
;

variable_declaration:
    type IDENTIFIER SEMICOLON
    | type IDENTIFIER ASSIGN expression SEMICOLON
;

type:
    INT | FLOAT | DOUBLE | CHAR | BOOLEAN
;

function_declaration:
    type IDENTIFIER LPAREN parameters RPAREN block
;

parameters:
    parameter
    | parameter COMMA parameters
    | /* empty */
;

parameter:
    type IDENTIFIER
    | type IDENTIFIER LBRACKET RBRACKET
    | type DOTDOTDOT IDENTIFIER
;

block:
    LBRACE declaration_list RBRACE
;

comment:
    // STRING
    | /* STRING */
;

expression:
    assignment
;

assignment:
    IDENTIFIER ASSIGN expression
    | IDENTIFIER PLUS ASSIGN expression
    | IDENTIFIER MINUS ASSIGN expression
    | IDENTIFIER TIMES ASSIGN expression
    | IDENTIFIER DIVIDE ASSIGN expression
    | IDENTIFIER MOD ASSIGN expression
    | IDENTIFIER AND ASSIGN expression
    | IDENTIFIER OR ASSIGN expression
;

struct_declaration:
    STRUCT IDENTIFIER LBRACE variable_declaration_list RBRACE SEMICOLON
;

variable_declaration_list:
    variable_declaration_list variable_declaration
    | /* empty */
;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main() {
    return yyparse();
}
