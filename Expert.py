#!/usr/local/bin/python3
import sys
import re
import Utils
import string
import Operation
from Rules import Rules

rules = Rules()

def handle_line(line):
    line = line.strip()
    if line and len(line) > 0:
        if line[0] == '=':
            rules.set_initials_facts(line)
        elif line[0] == '?':
            rules.set_question(line)
        else:
            rules.create_rules(line)


def open_file(path):
    try:
        file = open(path)
        for line in file:
            handle_line(line)
        file.close()
    except:
        Utils.end("Give me a real file please.")
    rules.solve()
    rules.print_answer()


if __name__ == '__main__':
    arg = sys.argv
    if (len(arg) != 2):
        Utils.end("usage: ./expert.py input_file")
    else:
        open_file(arg[1])
