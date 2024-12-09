grammar PythonSubset;

// Start rule
program: statement+ EOF;

// Statements
statement: com
         | assignment
         | expr
         | ifStatement
         | whileLoop
         | forLoop
         ;

// Assignment
assignment: IDENTIFIER ASSIGN expr
          | IDENTIFIER compoundAssign expr;

// if, elif, else statements
ifStatement: IF expr ':' (statement)+ (ELIF expr ':' statement+)* (ELSE ':' assignment+)*;

// while loops
whileLoop: WHILE expr ':' (statement)+;

// for loops
forLoop: FOR IDENTIFIER IN (expr | 'range') ':' (statement)+;

// Expressions
expr: '(' expr ')'
    | (TRUE | FALSE)
    | INT
    | FLOAT
    | STRING
    | IDENTIFIER
    | array
    | expr op=('*' | '/' | '%') expr
    | expr op=('+' | '-') expr
    | expr op=('<' |'<=' | '>' | '>=' | '==' | '!=' | AND | OR) expr
    | NOT expr
    ;

com : COMMENT | BLOCK_COMMENT ;

compoundAssign: '+=' | '-=' | '*=' | '/=';

// Array
array: '[' (expr (',' expr)*)? ']';


// Tokens
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
ASSIGN: '=';
INT: '-'?[0-9]+;
FLOAT: '-'?[0-9]+ '.' [0-9]+;
STRING: '\'' .*? '\'' | '"' .*? '"';
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
WS: [ \t\r\n]+ -> skip;
COMMENT: '#' ~[\r\n]* -> skip;
BLOCK_COMMENT : '\'\'\'' ( . | '\r' | '\n' )*? '\'\'\''
        -> channel(HIDDEN) ;
