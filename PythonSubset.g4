grammar PythonSubset;

// Start rule
program: statement+ EOF;

// Statements
statement: assignment
         | expr;

// Assignment
assignment: IDENTIFIER ASSIGN expr
          | IDENTIFIER compoundAssign expr;

// Expressions
expr: expr op=('*' | '/' | '%') expr
    | expr op=('+' | '-') expr
    | '(' expr ')'
    | IDENTIFIER
    | INT
    | FLOAT
    | STRING
    | array;


compoundAssign: '+=' | '-=' | '*=' | '/=';

// Array
array: '[' (expr (',' expr)*)? ']';

// Tokens
ASSIGN: '=';
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"';
WS: [ \t\r\n]+ -> skip;
