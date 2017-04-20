'''
    This class contains methods for parsing and executing base16 ancoded instruction sets.
    Instructions matrix: http://www.atarimagazines.com/computeii/issue3/page52.php
'''
from archi import *

class RCA1802(object):

    def __init__(self, memaddr):
        self.memaddr = memaddr

    def decode_inst(self):
        for reg in self.memaddr:
            if reg[0] == "1":
                return
            elif reg[0] == "2":
                return
            elif reg[0] == 
        
    def parse_inst():
        return
    '''
        Further branching out into more specifing opcodes execution
    '''


###END OF FILE###########################################################
