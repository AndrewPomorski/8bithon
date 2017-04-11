from memflow import check_free_bytes

'''
MEMORY CAPACITY for following registers
'''
global MEMCAP
MEMCAP = [0] * 256

'''
FREE BYTES  - keeps track of how many addresses in registry are free
'''
global FBYTES
FBYTES = check_free_bytes(MEMCAP)
