import ply.lex as lex

#reserved words
reserved = (
        'SET',
        'DRAW',
        'RAND',
        'MOV',
        'JMP',
)

tokens = reserved + (
        #registers from v0 to vF
        'REG',
        #HEX values from 0x0000 to 0x1000
        'ADDR',
        'COMMA',
        'NEWLINE',
        'ID',
        'COMMENT'
)

t_ignore = ' \t'



#Regex definitions for tokens.
t_COMMA = r'\,'
t_ADDR  = r'0[x][0-9A-F]+'

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t

def t_REG(t):
    r'v[0-9A-F]'
    return t

def t_COMMENT(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    pass


reserved_map = {}
for r in reserved:
    reserved_map[r.lower()] = r
def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value, "ID")
    return t

def t_preprocessor(t):
    r'\#(.)*?\n'
    t.lexer.lineno += 1

#def error behavior
def t_error(t):
    print("Illegal character '%s'" % t.value[0] )
    t.lexer.skip(1)

lexer = lex.lex()

########TESTS#########
data = '''
set     v0, 0x0 
set     v1, 0x0
draw    v0, v1
rand    v3, 0xF
mov     v0, vF
jmp     0x001
'''

registers = '''
v0
v1
v2 
v3 
v4'''

lexer.input(data)

#Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break #no more input
    print(tok)
#######ENDTEST#########
