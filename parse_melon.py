#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

## Cliente del analizador sintactico para el Lenguaje MeLon

import sys
from lexer import *
from parser import *

import ply.lex as lex
import ply.yacc as yacc

filename = raw_input("")
# Abrimos el archivo para lectura
try:
    f = open(filename,"r")
except IOError:
    print 'ERROR. No se pudo abrir el archivo' , filename
    sys.exit()

data = f.read()

# Se contruye el objeto Lexer
l = lex.lex()

# Se le da al lexer la entrada
l.input(data)

# Build the parser
parser = yacc.yacc()

result = parser.parse(data,lexer=l)
print result.info
