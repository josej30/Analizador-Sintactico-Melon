
# Lista de Tokens para el Lexer
tokens = (
   'IF',
   'FI',
   'THEN',
   'ELSE',
   'FUN',
   'NUF',
   'TRUE',
   'FALSE',
   'TEL',
   'LET',
   'IN',
   'DOSPUNTOS',
   'FLECHA',
   'LE',
   'GE',
   'NE',
   'OR',
   'AND',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'APAREN',
   'CPAREN',
   'LISTA',
   'EQ',
   'LT',
   'GT',
   'PIPE',
   'NOT',
   'NUMBER',
   'ID'
)

# Lista de palabras reservadas
reservadas = {
   'if' : 'IF',
   'fi' : 'FI',
   'then' : 'THEN',
   'else' : 'ELSE',
   'fun' : 'FUN',
   'nuf' : 'NUF',
   'nuf' : 'NUF',
   'true' : 'TRUE',
   'false' : 'FALSE',
   'let' : 'LET',
   'tel' : 'TEL',
   'in' : 'IN'
}

# Expresiones regulares para cada uno de los tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_APAREN  = r'\('
t_CPAREN  = r'\)'
t_DOSPUNTOS = r'::'
t_FLECHA = r'->'
t_LISTA = r'\[\]'
t_LE = r'<='
t_GE = r'>='
t_NE = r'<>'
t_OR = r'\\/'
t_AND = r'/\\'
t_EQ = r'='
t_LT = r'<'
t_GT = r'>'
t_NOT = r'!'
t_PIPE = r'\|'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = reservadas.get(t.value,'ID')
    return t

# La regla que permite hacer los saltos de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.lexpos = 0

# El string que contiene los caracteres que queremos ignorar
t_ignore  = ' \t'

# Regla para el caso de encontrar un error lexicografico
def t_error(t):
    print 'Caracter no reconocido '+t.value[0]+' en la linea '+str(t.lineno)
    sys.exit()
