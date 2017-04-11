'''
MEMORY CAPACITY for following registers
'''
global MEMCAP
MEMCAP = [0] * 256

'''
FREE BYTES  - keeps track of how many addresses in registry are free
'''
from memflow import check_free_bytes
global FBYTES
FBYTES = check_free_bytes(MEMCAP)
