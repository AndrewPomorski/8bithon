import sys
import time
import random
import lexer
import ply.yacc as yacc

tokens = lexer.tokens

def p_error(p):
    print "PARSING ERROR"

def p_expression_set(p):
    '''
        expression : SET REG COMMA ADDR NEWLINE
    '''
    print "Set expression found"

def p_expression_mov(p):
    '''
        expression : MOV REG COMMA REG NEWLINE
    '''
    print "Mov expression found"

def p_expression_ife(p):
    '''
        expression : IFE REG COMMA ADDR NEWLINE 
    '''
    print "if equals expression found"

def p_expression_ifn(p):
    '''
        expression : IFN REG COMMA ADDR NEWLINE
    '''
    print "if not equals expression found"

def p_expression_ifr(p):
    '''
        expression : IFR REG COMMA REG NEWLINE
    '''
    print "comparse registers expression found"

def p_expression_jmp(p):
    '''
        expression : JMP ADDR NEWLINE
    '''
    print "Jump statement found"

parser = yacc.yacc()

def parse_asm(data):
    parser.parse(data)
