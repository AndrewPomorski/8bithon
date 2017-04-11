import sys
import time
from ARCH import MEM
from GLOBALS import * 
from memflow import * 

def parse_alloc_val(acc):
	acc = acc.split('x')
	val = acc[0]
	addr = acc[1]
	if addr == '':
		addr = 'DEF_ADDR'
	buff = [val, addr]
	return buff

def malloc(acc_command):
	FREE_MEM = memflow.check_free_bytes()
	if FREE_MEM <= 0:
		print 'No free memory left. Aborting...' 
		return
	mem_buff = parse_alloc_val(acc_command)
	ALLOC_VAL = mem_buff[0]
	ALLOC_ADDR = mem_buff[1]
	for addr in MEM:
		if addr == ALLOC_ADDR:
			addr = ALLOC_VAL
	return

	'''
	At the end of this function is needed a substraction of free memory counter. 
	By default 256 (when initialized)
	At the end of each malloc cycle 1 mem addr is substracted. TODO: Behaviour on full memory

	'''	

'''
addr_def = '00011101x00011010'	
addr_ndef = '00011010x' 	
malloc(addr_def)
malloc(addr_ndef)
'''
