from _globals import MEMCAP

def free(address):
	freed = False
	for register in MEMCAP:
		if register == address:
			register = 0
			freed = True
		elif not address in MEMCAP:
			print('Could not find address: ', address)
			raise AllocError
