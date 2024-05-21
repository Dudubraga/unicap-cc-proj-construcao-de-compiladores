%{
#include "parser.tab.h"
%}

%%
"int"           return INT;
"float"         return FLOAT;
"double"        return DOUBLE;
"char"          return CHAR;
"boolean"       return BOOLEAN;
"if"            return IF;
"else"          return ELSE;
"while"         return WHILE;
"for"           return FOR;
"switch"        return SWITCH;
"case"          return CASE;
"default"       return DEFAULT;
"break"         return BREAK;
"continue"      return CONTINUE;
"return"        return RETURN;
"struct"        return STRUCT;
"&&"            return AND;
"||"            return OR;
"!"             return NOT;
"=="            return EQ;
"!="            return NEQ;
">="            return GE;
"<="            return LE;
">"             return GT;
"<"             return LT;
"+"             return PLUS;
"-"             return MINUS;
"*"             return TIMES;
"/"             return DIVIDE;
"%"             return MOD;
"="             return ASSIGN;
"("             return LPAREN;
")"             return RPAREN;
"{"             return LBRACE;
"}"             return RBRACE;
"["             return LBRACKET;
"]"             return RBRACKET;
";"             return SEMICOLON;
","             return COMMA;
"."             return DOT;
"->"            return ARROW;
"/*"            { BEGIN(COMMENT); }
<COMMENT>"*/"   { BEGIN(INITIAL); }
<COMMENT>.      /* ignore comments */
<COMMENT>\n     /* ignore comments */
"//".*          /* ignore comments */
[0-9]+          return NUM_INT;
[0-9]+"."[0-9]+ return NUM_DEC;
[a-zA-Z_][a-zA-Z0-9_]* return IDENTIFIER;
\"[^\"]*\"      { yylval.string = strdup(yytext); return STRING; }
[ \t\n]+        /* ignore whitespace */;
.               return yytext[0];
%%

int yywrap() {
    return 1;
}
