grammar PythonSubset;

program
    : stmt* EOF
    ;

stmt
    : simpleStmt
    | compoundStmt
    | NEWLINE
    ;

simpleStmt
    : (assignment | expr) NEWLINE
    | COMMENT NEWLINE
    | MULTILINE_COMMENT NEWLINE
    ;

compoundStmt
    : if_stmt
    | while_stmt
    | for_stmt
    ;

if_stmt
    : IF expr ':' NEWLINE suite
      (ELIF expr ':' NEWLINE suite)*
      (ELSE ':' NEWLINE suite)?
    ;

while_stmt
    : WHILE expr ':' NEWLINE suite
    ;

for_stmt
    : FOR IDENTIFIER IN expr ':' NEWLINE suite
    ;

suite
    : INDENT stmt+ DEDENT NEWLINE?
    ;

assignment
    : IDENTIFIER ASSIGN expr
    | IDENTIFIER compoundAssign expr
    ;

expr
    : '(' expr ')'                                    
    | NOT expr                                        
    | expr (MULTIPLY | DIVIDE | MODULO) expr         
    | expr (PLUS | MINUS) expr                       
    | expr (GT | GTE | LT | LTE | EQUALS | NOT_EQUALS) expr
    | expr AND expr                                  
    | expr OR expr                                   
    | atom                                           
    ;

atom
    : TRUE
    | FALSE
    | INT
    | FLOAT
    | STRING
    | IDENTIFIER
    | array
    | functionCall
    ;

functionCall
    : IDENTIFIER '(' (expr (',' expr)*)? ')'
    ;

array
    : '[' (expr (',' expr)*)? ']'
    ;

compoundAssign
    : '+='
    | '-='
    | '*='
    | '/='
    ;

// Keywords
TRUE: 'True';
FALSE: 'False';
AND: 'and';
OR: 'or';
NOT: 'not';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
WHILE: 'while';
FOR: 'for';
IN: 'in';

// Operators
ASSIGN: '=';
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
MODULO: '%';
GT: '>';
GTE: '>=';
LT: '<';
LTE: '<=';
EQUALS: '==';
NOT_EQUALS: '!=';

// Indentation
INDENT: 'INDENT';
DEDENT: 'DEDENT';

// Literals
INT: '-'?[0-9]+;
FLOAT: '-'?[0-9]+ '.' [0-9]+;
STRING: '\'' (~[\r\n'])* '\'' | '"' (~[\r\n"])* '"';
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;

// Comments
COMMENT: '#' ~[\r\n]*;
MULTILINE_COMMENT: '\'\'\'' .*? '\'\'\'';

// Whitespace
NEWLINE: [\r\n]+;
WS: [ \t]+ -> skip;