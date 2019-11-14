from Operation import Fact, Operation
import Utils

SIDE = Utils.Side

class Rules:
	def __init__(self):
		self.operations = []
		self.facts = []

	def set_initials_facts(self, string):

		print("Setting facts : " + string)
		for c in string:
			for f in self.facts:
				if c == f.name :
					f.value = 1
					f.set = True
					print("Fact set : " + f.name)

	def print_questions(self, string):
		print("Setting questions : " + string)
		for c in string:
			for f in self.facts:
				if c == f.name :
					print(f.name + " : ", f.value)

	def create_rules(self, string):
		for op_main in Utils.MAIN_OPERATOR:
			if string.find(op_main) > 0: 
				self.create_operation(string.split(op_main), op_main, SIDE.MOTHER)

	def create_operation(self, array_string, operator, side):
    	
		print(array_string[0] + operator + array_string[1])
		self.check_side(array_string[0], SIDE.LEFT)
		self.check_side(array_string[1], SIDE.RIGHT)
		return 

	def add_fact_if_not_existing(self, name):
		for f in self.facts:
			if f.name == name:
				return f
		fact = Fact(name)
		print("Adding Fact not creacted : " + fact.name)
		self.facts.append(fact)
		return fact

	def push(self, obj, l, depth):
		while depth:
			l = l[-1]
			depth -= 1
		print(obj)
		l.append(obj)

	def parse_parentheses(self, s):
		op = ""
		groups = []
		depth = 0
		md = 0
		for char in s:
			if char == '(':
				if len(op) > 0:
    					groups.append([op, depth - 1])
				op = ""
				depth += 1
			elif char == ')':
				depth -= 1
				if depth > md : md = depth
				groups.append([op, depth])
				op = ""
			else:
				op += char
		return groups, md

	def check_side(self, string, side):
		if string.find('(') != -1:
			print("jai des parenthese a index :" + str(string.find('(')) + str(string.rfind(')')))
			groups, depth = self.parse_parentheses(string)
			print("deth : " + str(depth))
			i = 0
			while i < len(groups):
				print(groups[i][0], groups[i][1] == depth)
				if groups[i][1] == depth:
					groups[i][1] = depth - 1
					print("yo")
				i += 1
			for g in groups:
    				print(g[0], g[1] == depth)
			
			return
		# define if op or fact

	def solve(self):
		# solving array of op
		print("solving")