%{
#include "y.tab.h"
%}

%%

int             { return INT; }
float           { return FLOAT; }
double          { return DOUBLE; }
char            { return CHAR; }
boolean         { return BOOLEAN; }
struct          { return STRUCT; }
if              { return IF; }
else            { return ELSE; }
while           { return WHILE; }
for             { return FOR; }
switch          { return SWITCH; }
case            { return CASE; }
default         { return DEFAULT; }
break           { return BREAK; }
continue        { return CONTINUE; }
return          { return RETURN; }
[0-9]+          { yylval = atoi(yytext); return NUM_INT; }
[0-9]+"."[0-9]* { yylval = atof(yytext); return NUM_DEC; }
\"[^"\n]*\"     { return TEXTO; }
[a-zA-Z_][a-zA-Z_0-9]* { yylval = strdup(yytext); return ID; }
"//"[^"\n]*     { /* ignore single line comments */ }
"/*".*"*/"      { /* ignore multi-line comments */ }
[ \t\r\n]+      { /* ignore whitespace */ }
.               { return yytext[0]; }

%%
