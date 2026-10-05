grammar nerock;

prog: command+ EOF;
command: func_decleration  | expr | decl_var | return | importScript;

block: '{' command* '}';


// decl main()
func_decleration: DECL_FUNC
    ID
    paramList
    returnFunc
    block
    ;

decl_var: 'var' ID typesKeyword '=' expr;

call: ID '(' (expr (',' expr)*)? ')';


expr: call
    | atom
    | '-' expr
    | expr (DIV | MUL) expr
    | expr (PLUS | MIN) expr
    | expr (BIGGER_L | LOWER_L) expr
    | expr EQUAL_C expr
    ;

typesKeyword: INT_TYPE | STRING_TYPE | FLOAT_TYPE | VOID_TYPE | BOOL_TYPE;

importScript: 'declare' ID;

param: typesKeyword ID;

paramList: '(' (param (',' param)*)? ')';
returnFunc: ('->' typesKeyword)?;

atom: NUM | FLOAT | STRING | ID;

return: 'return' expr;

// Operators
PLUS: '+';
MIN: '-';
MUL: '*';
DIV: '/';

BIGGER_L: '>';
LOWER_L: '<';
EQUAL_C: '==';

// Keywords
DECL_FUNC: 'decl';
INT_TYPE : 'i32';
STRING_TYPE : 'str';
FLOAT_TYPE : 'f32';
BOOL_TYPE : 'i1';
VOID_TYPE : 'v';

// Tokens
ID : [a-zA-Z][a-zA-Z0-9_]*;
FLOAT : [0-9]+ '.' [0-9]+;
NUM   : [0-9]+;
COMMENT : '#' ~[\r\n]* -> skip;
STRING : '"' ~[\r\n"]* '"'
       | '\'' ~[\r\n']* '\''
       ;

WS : [ \t\r\n]+ -> skip;