# Get the token map from the lexer.  This is required.
from lexer import tokens
import sys
from arbol import *

precedence = (
    ('nonassoc','LE','GE','GT','LT','EQ','NE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'AND', 'OR'),
    ('right', 'NOT'),
    ('right', 'DOSPUNTOS'),
)

def p_arit(p):
    '''expression : expression MINUS expression
                | expression PLUS expression
                | expression TIMES expression
                | expression DIVIDE expression
                | constantes
                | variables'''
    if (len(p)>2):
        if (p[2] == '+'):
#            p[0] = "(MAS "+p[1]+" "+p[3]+" )"
            p[0] = Nodo([p[1],p[3]],"(MAS "+p[1].info+" "+p[3].info+")")
        elif (p[2] == '-'):
#            p[0] = "(MENOS "+p[1]+" "+p[3]+" )"
            p[0] = Nodo([p[1],p[3]],"MENOS")
        elif (p[2] == '*'):
#            p[0] = "(PRODUCTO "+p[1]+" "+p[3]+" )"
            p[0] = Nodo([p[1],p[3]],"PRODUCTO")
        elif (p[2] == '/'):
#            p[0] = "(COCIENTE "+p[1]+" "+p[3]+" )"
            p[0] = Nodo([p[1],p[3]],"COCIENTE")
    else:
        p[0] = Nodo([p[1]],p[1])
#        p[0] = p[1]

def p_bool(p):
    '''expression : expression AND expression
                  | expression OR expression
                  | expression GT expression
                  | expression LT expression
                  | expression EQ expression
                  | expression NE expression
                  | expression GE expression
                  | expression LE expression
                  | NOT expression'''

    if (len(p) == 4):
        if (p[2] == '/\\'):
            p[0] = "(AND "+p[1]+" "+p[3]+")"
        elif (p[2] == '\\/'):
            p[0] = "(OR "+p[1]+" "+p[3]+")"
        elif (p[2] == '>'):
            p[0] = "(MAYOR "+p[1]+" "+p[3]+")"
        elif (p[2] == '<'):
            p[0] = "(MENOR "+p[1]+" "+p[3]+")"
        elif (p[2] == '='):
            p[0] = "(IGUAL "+p[1]+" "+p[3]+")"
        elif (p[2] == '<>'):
            p[0] = "(DISTINTO "+p[1]+" "+p[3]+")"
        elif (p[2] == '<='):
            p[0] = "(MENORIGUAL "+p[1]+" "+p[3]+")"
        elif (p[2] == '>='):
            p[0] = "(MAYORIGUAL "+p[1]+" "+p[3]+")"
    else:
        p[0] = "(NO "+p[2]+")"            

def p_if(p):
    'expression : IF expression THEN expression ELSE expression FI'
    p[0] = "(IF "+p[2]+" "+p[4]+" "+p[6]+")"

def p_par_exp(p):
    'expression : APAREN expression CPAREN'
    p[0] = "("+p[2]+")"

def p_listav(p):
    'expression : LISTA'
    p[0] = "(LISTAVACIA)"

def p_patron(p):
    '''patron : constantes
              | variables 
              | patron DOSPUNTOS patron
              | APAREN patron CPAREN
              '''
    if (len(p) > 2):
        if (p[2] == '::'):
            p[0] = "(LISTA "+p[1]+" "+p[3]+")"
        else:
            p[0] = "("+p[2]+")"            
    else:
        p[0] = "(PATRON "+p[1]+")"

def p_var(p):
    'variables : ID'
    p[0] = "(VARIABLE "+p[1].upper()+")"

def p_cons(p):
    '''constantes : number
                  | false
                  | true'''
    p[0] = p[1]

def p_number(p):
    'number : NUMBER'
    p[0] = "(ENTERO "+str(p[1])+")"

def p_true(p):
    'true : TRUE'
    p[0] = "(BOOLEANO "+p[1].upper()+")"

def p_false(p):
    'false : FALSE'
    p[0] = "(BOOLEANO "+p[1].upper()+")"

def p_let(p):
    'expression : LET patron EQ expression IN expression TEL'
    p[0] = "(LET "+p[2]+" "+p[4]+" "+p[6]+")"

## Funciones que contienen las gramaticas para el
## caso de FUN y sus funciones auxiliares

def p_fun(p):
    'expression : FUN gen NUF'
    p[0] = "(FUN "+p[2]+")"

def p_listapat(p):
    '''listapat : listapat patron
                | patron
    '''
    if (len(p)>2):
        p[0] = p[1] + " " + p[2]
    else:
        p[0] = p[1]

def p_nproduc(p):
    '''gen : listapat FLECHA expression
           | gen PIPE listapat FLECHA expression
    '''
    if (len(p) == 4):
        p[0] = p[1] + " " + p[3]
    else:
        p[0] = p[1] + " " + p[3] + " " + p[5]

# Error rule for syntax errors
def p_error(p):
    print "Syntax error in input!"
    sys.exit()
