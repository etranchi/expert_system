#!/Users/etranchi/.brew/bin/python3
import sys
import re
import Utils
import string
import Struct


facts = []
operations = []


def create_op(line):
	for op_main in Struct.MAIN_OPERATOR:
		print(op_main)
		index = line.index(op_main)
		print(index)
	print("yo")

def handle_line(line):
	try :
		line = line.translate({ord(c): None for c in string.whitespace}).split('#')[0]
		print("Line cleaned : " + line)
		if len(line) > 0:
			create_op(line)
	except:
		Utils.end("Erreur parsing.")


def open_file(path):
	try:
		file = open(path)
		for line in file:
			handle_line(line)
		print("I got everything needed.")
		file.close()
	except:
		Utils.end("Give me a real file please.")




if __name__ == '__main__':
    arg = sys.argv
    if (len(arg) != 2):
        Utils.end("usage: ./expert.py input_file")
    else:
        open_file(arg[1])