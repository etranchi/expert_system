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
		operation = Operation(operator, array_string, side)
		operation.left = self.check_side(array_string[0], SIDE.LEFT)
		operation.right = self.check_side(array_string[1], SIDE.RIGHT if operator == "=>" else SIDE.LEFT)
		self.operations.append(operation)
		return operation

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
		l.append(obj)

	def parse_parentheses(self, s):
		groups = []
		depth = 0

		for char in s:
			if char == '(':
				self.push([], groups, depth)
				depth += 1
			elif char == ')':
				depth -= 1
			else:
				self.push(char, groups, depth)
		return groups

	def check_side(self, string, side):
		if string.find('(') != -1:
			print("jai des parenthese a index :" + str(string.find('(')) + str(string.rfind(')')))
			groups = self.parse_parentheses(string)
			print(groups, "group 0")
			print(groups[0], "group 0")
			for g in groups[0]:
				print(g)
			return
		for op in Utils.OPERATOR:
			if string.find(op) > 0:
				return self.create_operation(string.split(op), op, side)
		print("creating fact name : " + string)
		return self.add_fact_if_not_existing(string)
		# define if op or fact

	def solve(self):
		# solving array of op
		print("solving")