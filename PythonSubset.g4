grammar PythonSubset;

// Start rule
program: statement+ EOF;

// Statements
statement: simpleStatement NEWLINE
    | compoundStatement
    ;

simpleStatement: assignment
    | expr
    ;

compoundStatement: ifStatement
    | whileStatement
    | forStatement
    ;

// Assignment
assignment: IDENTIFIER ASSIGN expr
          | IDENTIFIER compoundAssign expr;

// Control Structures
ifStatement: IF expr ':' (assignment)+ (ELIF expr ':' assignment+)* (ELSE ':' assignment+)?;

whileStatement: WHILE condition COLON suite;

forStatement: FOR IDENTIFIER IN expr COLON suite;

suite: simpleStatement
    | NEWLINE INDENT statement+ DEDENT;

condition: expr;

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
COLON: ':'; 
ASSIGN: '=';
INT: '-'?[0-9]+;
FLOAT: '-'?[0-9]+ '.' [0-9]+;
STRING: '\'' .*? '\'' | '"' .*? '"';
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
NEWLINE: ('\r'? '\n' | '\r') SPACES?;
SPACES: [ \t]+;
WS: [ \t]+ -> skip;
INDENT: 'INDENT' -> skip;
DEDENT: 'DEDENT' -> skip;
COMMENT: '#' ~[\r\n]* -> skip;
LINE_JOINING: '\\' NEWLINE -> skip;
