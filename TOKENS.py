from maths import *
from free import *
from _globals import *
ADD = add_HX
SUB = sub_HX
MUL = mul_HX
DIV = div_HX
FREE = free

'''
MV - move value from one address to another
ASN - assign value to variable
'''

TOKENSLIST = {ADD: 2, SUB: 2, MUL: 2, DIV: 2, FREE: 1}

for key, value in TOKENSLIST.iteritems():
	print('Current key:',key, 'Current value:', value)


