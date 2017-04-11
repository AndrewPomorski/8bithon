import sys
from TOKENS import *

def file_entry():
	try:	
		in_file_name = sys.argv[1]
		with open(sys.argv[1], 'r') as file:
			input_data = file.rad().replace('\n','')
			'''
			tokenization purposes, might be changed
			'''
			input_data = list(input_data)
			return [input_data, in_file_name]
	except IndexError:
		print 'No input file'


if __name__ == '__main__':
	data = file_entry()
	
