'''
    Whenever font package is updated run this program on the *.pff file
'''
import sys
hexedfonts = []

with open(sys.argv[1]) as pff:
    BinFont = pff.read().split("\n")


#for some reason the last pos is empty
BinFont = filter(None, BinFont)
for val in BinFont:
    hexedfonts.append(hex(int(val, 2)))


outfile = open('outfont.hff', 'w')
for hex in hexedfonts:
    lineval = hex + '\n'
    outfile.write(lineval)


