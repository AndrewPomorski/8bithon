import sys
import lexer
import parseasm

source = open(sys.argv[1], 'r')
data = source.read()

with open(sys.argv[1], 'r') as data:
    for line in data:
        try:
            parseasm.parse_asm(line)
        except EOFError:
            break
