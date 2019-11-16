from Operation import Fact, Operation
import Utils
import Parser

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
					print("Fact set : " + f.name)

	def print_questions(self, string):
		print("Setting questions : " + string)
		for c in string:
			for f in self.facts:
				if c == f.name :
					print(f.name + " : ", f.value)

	def create_rules(self, string):
		# splitting expression : array[0] => array[1]
		for op_main in Utils.MAIN_OPERATOR:
			if string.find(op_main) > 0: 
				self.create_operation(string.split(op_main))

	def create_operation(self, array_string):
		op = Operation(array_string[0], array_string[1])
		self.operations.append(op)
		print(Parser.shunting(Parser.get_input(array_string[0])))


	def create_fact_if_not_existing(self, name):
		for f in self.facts:
			if f.name == name:
				return f
		fact = Fact(name)
		print("Adding Fact not creacted : " + fact.name)
		self.facts.append(fact)
		return fact

	def check_side(self, s, side):
		print(s + "before parsing")
		calc = Parser.shunting(Parser.get_input(s))
		print(calc)
		return None

	def solve(self):
		# solving array of op
		print("solving")