grammar nerock;

prog: command+ EOF;
command: func_decleration  | expr | decl_var;

block: '{' command* '}';

// decl main()
func_decleration: DECL_FUNC
    ID
    paramList
    returnFunc
    block
    ;

decl_var: 'var' ID typesKeyword '=' expr;

expr: ID '(' (expr (',' expr)*)? ')'
    | atom
    | expr MUL expr
    | expr DIV expr
    | expr PLUS expr
    | expr MIN expr
    ;

typesKeyword: INT_TYPE | STRING_TYPE | FLOAT_TYPE | VOID_TYPE;

param: typesKeyword ID;

paramList: '(' (param (',' param)*)? ')';
returnFunc: ('->' typesKeyword)?;

atom: NUM | FLOAT | STRING | ID;

// Operators
PLUS: '+';
MIN: '-';
MUL: '*';
DIV: '/';

// Keywords
DECL_FUNC: 'decl';
INT_TYPE : 'i32';
STRING_TYPE : 'str';
FLOAT_TYPE : 'f32';
VOID_TYPE : 'v';

// Tokens
ID : [a-zA-Z][a-zA-Z0-9_]*;
FLOAT : '-'? [0-9]+ '.' [0-9]+;
NUM : '0' | '-'? [1-9][0-9]*;
COMMENT : '#' ~[\r\n]* -> skip;
STRING : '"' ~[\r\n"]* '"'
       | '\'' ~[\r\n']* '\''
       ;

WS : [ \t\r\n]+ -> skip;