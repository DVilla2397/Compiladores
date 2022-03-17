grammar marzo;
program: (expression | statement)+;

expression:

	expression comparator = IGUAL expression	
    | expression comparator = MAYOR expression
	| expression comparator = MENOR expression			
	

	| expression operator = SUMAR expression			
    | expression operator = MULTIPLICAR expression		
	| expression operator = RESTAR expression	
	| expression operator = DIVIDIR expression		
	| expression operator = PORCENTAJE expression			
	| '(' expression ')'							
	
	| INT 
	
	| VAR;

statement:
	
	VAR assigner = AS expression			
	| VAR assigner = SUMAR_AS expression		
	| VAR assigner = DIVIDIR_AS expression	
	| VAR assigner = MODULO_AS expression	
	| VAR assigner = MULTIPLICAR_AS expression	
	
	| 'int' VAR # declare_int;


VAR: [a-z_][A-z0-9_]+;


INT: [0-9]+;

IGUAL: '==';
MAYOR: '>';
MENOR: '<';

SUMAR: '+';
MULTIPLICAR: '*';
RESTAR: '-';
DIVIDIR: '/';
PORCENTAJE: '%';

AS: '=';
SUMAR_AS: '+=';
DIVIDIR_AS: '/=';
MODULO_AS: '%=';
MULTIPLICAR_AS: '*=';