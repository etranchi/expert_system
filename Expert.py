#!/usr/local/bin/python3
import sys
import re
import Utils
import string
import Operation
from Rules import Rules

rules = Rules()
SIDE = Utils.Side

def handle_line(line):
	try :
		line = line.translate({ord(c): None for c in string.whitespace}).split('#')[0]
		print(line)
		if line and len(line) > 0:
			if line[0] == '=':
				rules.set_initials_facts(line)
			elif line[0] == '?':
				rules.print_questions(line)
			else:
				rules.create_rules(line)
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
	for f in rules.facts:
		print(f.name, f.value, f.set)
	for op in rules.operations:
		if op.side == SIDE.LEFT:
			op.is_possible_to_make()




if __name__ == '__main__':
    arg = sys.argv
    if (len(arg) != 2):
        Utils.end("usage: ./expert.py input_file")
    else:
        open_file(arg[1])