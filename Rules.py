from Operation import Fact, Operation
import Utils
import Parser
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
		# self.check_side(string, SIDE.MOTHER)
		for op_main in Utils.MAIN_OPERATOR:
			if string.find(op_main) > 0: 
				self.create_operation(string.split(op_main), op_main, SIDE.MOTHER)

	def create_operation(self, array_string, operator, side):
    	
		#print(array_string[0] + operator + array_string[1])
		self.check_side(array_string[0], SIDE.LEFT)
		#self.check_side(array_string[1], SIDE.RIGHT)
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
		l.append(obj)

	def parse_parentheses(self,s):
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

	def make_op(self, op):
		print("making op", op)
		newop = Operation(op[1], op, self.add_fact_if_not_existing(op[0]), self.add_fact_if_not_existing(op[2]))
		# self.operations.append(newop)
		return newop
	

	def check_side(self, s, side):
		print(s + "before parsing")
		calc = Parser.shunting(Parser.get_input(s))
		print(calc)
		return None
		# define if op or fact

	def solve(self):
		# solving array of op
		print("solving")