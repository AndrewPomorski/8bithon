def convert_hex_dec(hex_num):
	return int(hex_num, 16)

def add_HX(numA, numB):
	num_buff = [numA, numB]
	dec_nums_buff = []
	for hexnum in num_buff:
		dec_nums_buff.append(convert_hex_dec(hexnum))
	SUM = dec_nums_buff[0] + dec_nums_buff[1]
	return SUM

def mul_HX(numA, numB):	
	num_buff = [numA, numB]
	dec_nums_buff = []
	for hexnum in num_buff:
		dec_nums_buff.append(convert_hex_dec(hexnum))
	PROD = dec_nums_buff[0] * dec_nums_buff[1]
	return PROD


def div_HX(numA, numB):	
	num_buff = [numA, numB]
	dec_nums_buff = []
	for hexnum in num_buff:
		dec_nums_buff.append(convert_hex_dec(hexnum))
	DIV = dec_nums_buff[0] / dec_nums_buff[1]
	return DIV


def sub_HX(numA, numB):	
	num_buff = [numA, numB]
	dec_nums_buff = []
	for hexnum in num_buff:
		dec_nums_buff.append(convert_hex_dec(hexnum))
	DIFF = dec_nums_buff[0] - dec_nums_buff[1]
	return DIFF
