# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# r'atring' -> r significa que la cadena es tradada sin caracteres de escape,
# es decir r'\n' seria un \ seguido de n (no se interpretaria como salto de linea)

# List of token names.   This is always required
reserved = {
    'vamosatomar': 'TYPE_INT',
    'verdadoreto': 'TYPE_BOOL',
    'whiskey': 'TYPE_WHILE',
    'flordecaña': 'TYPE_FOR',
    'simondice': 'TYPE_IF',
    'vodka': 'TYPE_VOID',
    'vomitame': 'TYPE_COUT',
    'pasapasa': 'TYPE_CIN',
    'findelaprevia': 'TYPE_ENDLIE',
    'mano': 'TYPE_MAIN',
    'regresaacasa': 'TYPE_RETURN',
    'fourloko': 'TYPE_FLOAT',
    'cartavio': 'TYPE_CHAR',
    'doublelabel': 'TYPE_DOUBLE',
    'smirnoff': 'TYPE_STRING',
    'sino': 'TYPE_ELSE',
    'jalemos': 'TYPE_BREAK',
    'fija': 'TYPE_CASE',
    'securris': 'TYPE_DO',
    'qsale': 'TYPE_SWITCH',
    'castigao': 'TYPE_DEFAULT',
}

tokens = [
    'NUMBER', 'DECIMAL', 'SUMA', 'RESTA', 'MULTIPLICACION', 'DIVIDE',
    'OPEN_PARENTESIS', 'CLOSE_PARENTESIS', 'EQUAL', 'OP_IGUAL', 'ID',
    'OPEN_KEY', 'CLOSE_KEY', 'OP_MAYOR_IGUAL', 'OP_MENOR_IGUAL',
    'OPEN_BRACKETS', 'CLOSE_BRACKETS', 'OP_PYC', 'OP_MAYOR', 'OP_MENOR',
    'OP_COMA', 'OP_AMPERSAND', 'OP_RESIDUO', 'LITERAL', 'OP_AGREGACION',
    'OP_DISMINUCION', 'OP_MOSTRAR', 'OP_INGRESAR'
] + list(reserved.values())

# Regular expression rules for simple tokens
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'\=='
t_OP_IGUAL = r'\='
t_OPEN_PARENTESIS = r'\('
t_CLOSE_PARENTESIS = r'\)'
t_OPEN_KEY = r'\{'
t_CLOSE_KEY = r'\}'
t_OP_MAYOR_IGUAL = r'\>='
t_OP_MENOR_IGUAL = r'\<='
t_OPEN_BRACKETS = r'\['
t_CLOSE_BRACKETS = r'\]'
t_OP_PYC = r'\;'
t_OP_MAYOR = r'\>'
t_OP_INGRESAR = r'\>>'
t_OP_MENOR = r'\<'
t_OP_MOSTRAR = r'\<<'
t_OP_COMA = r'\,'
t_OP_AMPERSAND = r'\&'
t_OP_RESIDUO = r'\%'
t_OP_AGREGACION = r'\++'
t_OP_DISMINUCION = r'\--'


#t_LITERAL r'(\'[^\']*\'|\"[^\"]*\")'
def t_LITERAL(t):
  r'(\'[^\']*\'|\"[^\"]*\")'
  t.value = t.value[1:-1]  # Quita las comillas del inicio y el final
  return t


# A regular expression rule with some action code
def t_ID(t):
  r'[a-zA-Z]+ ( [a-zA-Z0-9]* )'
  t.type = reserved.get(t.value, 'ID')  # Check for reserved words
  return t


#t_NUMBER  = r'\d+'
def t_NUMBER(t):
  r'\d+'
  t.value = int(t.value)  # guardamos el valor del lexema
  #print("se reconocio el numero")
  return t


def t_DECIMAL(t):
  r'\d+\.\d+'
  t.value = float(t.value)  # guardamos el valor del lexema
  #print("se reconocio el numero")
  return t


# Define a rule so we can track line numbers
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

with open('main1.as', 'r') as archivo:
  contenido = archivo.read()

# Give the lexer some input
#lexer.input(data)
#lexer.input (data2)
lexer.input(contenido)
# Tokenize
tokens_info = []


def lexico():
  while True:
    tok = lexer.token()
    if not tok:
      break
    token_info = {
        "symbol": tok.type,
        "lexema": tok.value,
        "lineno": tok.lineno,
        "lexpos": tok.lexpos
    }
    #print(token_info)
    tokens_info.append(token_info)
  dolar = [
      {
          "symbol": "$",
          "lexeme": "$",
          "nroline": 2,
          "col": 2
      },
  ]
  tokens_info.append(dolar)
  return tokens_info


#lexico()
